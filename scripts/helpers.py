from maya.OpenMaya import MVector
import maya.cmds as cmds
import sys
import math


def attributeExists(attr, node):
    '''
    recreation of the attributeExists command from mel

    Args:
        attr(string): the name of the attribute
        node(string): the name of the node to check for the attribute on

    Return:
    false if attribute isnt present, and true if it is
    '''
    if (attr and node):
        if not cmds.objExists(node):
            return 0
        if attr in cmds.listAttr(node, shortNames=True):
            return 1
        if attr in cmds.listAttr(node):
            return 1
        return 0


def polySelectBorderShell(borderOnly=False):
    '''
    recreation of the mel polySelectBorderShell command,
    selects the shell or the shell border of a selection.

    Args:
        borderOnly(boolean): if true return the border if false return the shell.

    Return:
        None
    '''

    subdComps = []

    if cmds.isTrue('subdivUIExists'):
        subdComps = cmds.subdListComponentConversion(fv=True, ff=True, fuv=True, fe=True, tuv=True)

        #Process only one type.
        subdComps = cmds.filterExpand(subdComps, ex=False, sm=73)
        if subdComps:
            #Convert selected Subd uvs to shell uvs or border
            if borderOnly:
                subdComps = cmds.subdListComponentConversion(subdComps, fuv=True, tuv=True, uvb=True)
                subdComps = cmds.subdListComponentConversion(subdComps, fuv=True, tuv=True, uvs=True)
            else:
                subdComps = cmds.subdListComponentConversion(subdComps, fuv=True, tuv=True, uvs=True)

    #turn on shell mode for selection.
    cmds.polySelectConstraint(t=0)
    cmds.polySelectConstraint(sh=1, bo=0, m=2)

    if borderOnly:
        #Only do one type. order of testing UVs vtx, face, edge.
        #UV
        compSel = cmds.filterExpand(ex=False, sm=35)
        if compSel:
            cmds.polySelectConstraint(t=0x0010, sh=0, bo=1, m=2)
            cmds.polySelectConstraint(t=0x0010, sh=1, bo=0, m=0)
        else:
            #Vertex
            compSel = cmds.filterExpand(ex=False, sm=31)
            if compSel:
                cmds.polySelectConstraint(w=1, t=0x0001, m=2)
                cmds.polySelectConstraint(w=0, t=0x0001, m=0)
            else:
                #Edge
                compSel = cmds.filterExpand(ex=False, sm=32)
                if compSel:
                    cmds.polySelectConstraint(w=1, t=0x8000, m=2)
                    cmds.polySelectConstraint(w=0, t=0x8000, m=0)
                else:
                    #face
                    compSel = cmds.filterExpand(ex=False, sm=34)
                    if compSel:
                        cmds.polySelectConstraint(w=1, t=0x0008, m=2)
                        cmds.polySelectConstraint(w=0, t=0x0008, m=0)

    #reset selection Constraints
    cmds.polySelectConstraint(sh=0, bo=0, m=0)

    #add selection to list of the subdcomponets
    if subdComps:
        cmds.select(subdComps, add=True)


def uvShellHardEdges():
    '''
    Sets uv border edges on a mesh has hard, and everythign else as soft.
    '''
    objList = cmds.ls(sl=True, o=True)
    finalBorder = []

    for subObj in objList:
        cmds.select(subObj, r=True)
        cmds.polyNormalPerVertex(ufn=True)
        cmds.polySoftEdge(subObj, a=180, ch=1)
        cmds.select(subObj + '.map[*]', r=True)

        polySelectBorderShell(borderOnly=True)

        uvBorder = cmds.polyListComponentConversion(te=True, internal=True)
        uvBorder = cmds.ls(uvBorder, fl=True)

        for curEdge in uvBorder:
            edgeUVs = cmds.polyListComponentConversion(curEdge, tuv=True)
            edgeUVs = cmds.ls(edgeUVs, fl=True)

            if len(edgeUVs) > 2:
                finalBorder.append(curEdge)

        cmds.polySoftEdge(finalBorder, a=0, ch=1)

    cmds.select(objList)


def xRayToggle():
    '''
    Toggles between XRay mode and shaded on a per object basis.
    '''
    sel = cmds.ls(sl=True, dag=True, ap=True, typ='surfaceShape')
    hilighted = cmds.ls(hl=True, dag=True, ap=True, typ='surfaceShape')

    for obj in hilighted:
        test = cmds.displaySurface(obj, q=True, xRay=True)
        hold = test[0]

        if hold:
            cmds.displaySurface(obj, xRay=False)
        else:
            cmds.displaySurface(obj, xRay=True)

    for obj in sel:
        test = cmds.displaySurface(obj, q=True, xRay=True)
        hold = test[0]

        if hold:
            cmds.displaySurface(obj, xRay=False)
        else:
            cmds.displaySurface(obj, xRay=True)


def facetoVertNRM():  # FIXME fix usage for faces bordering hard edges.
    '''
    sets the vertex normals of the verts contained in a face to that of the face.
    '''
    fs = cmds.filterExpand(sm=34)
    cmds.select(cl=True)
    for f in fs:
        cmds.select(f, r=True)
        normals = cmds.polyInfo(faceNormals=True)
        buf = str(normals).split()
        plane = range(3)
        plane[0] = float(buf[2])
        plane[1] = float(buf[3])
        plane[2] = float(buf[4].rstrip('\\n\']'))
        vtx = cmds.polyListComponentConversion(f, ff=True, tv=True)
        cmds.polyNormalPerVertex(vtx, xyz=[plane[0], plane[1], plane[2]])


def getFaces():
    '''
    Recreation of getFaces from mel
    Gets faces attached to the currently selected componet

    Args:
        None

    Return:
        result(list): list of the selected faces
    '''
    cmds.select(cmds.polyListComponentConversion(tf=True), r=True)
    result = cmds.filterExpand(ex=True, sm=34)
    return result


def getViewSize():
    '''
    Gets the size of the pane under the cursor and retruns
    it as a array index 0 is x axis and index 1 is y axis
    '''
    viewPanel = cmds.getPanel(underPointer=True)
    size = [0, 0]
    size[0] = cmds.control(viewPanel, q=True, w=True)
    size[1] = cmds.control(viewPanel, q=True, h=True)
    return size


def polyChamferVtx(doHist=True, width=0.5, deleteFace=False):
    '''
    Recreation of the polyChamferVtx from mel
    performs a vertex extrude, than locks the length and division values and deletes the vtx
    to emulate a vertex chamfer

    Args:
        dohist(boolean): create history or not
        width(float): the width of the vertex chamfer
        deleteFace(boolean): delete result face or not.

    Returns:
        node(string): the resulting node
    '''
    result = cmds.polyExtrudeVertex(ch=doHist, length=0, divisions=1, width=width)
    if len(result) > 0:
        node = [None]
        cmds.setAttr(result[0] + '.divisions', lock=True)
        cmds.setAttr(result[0] + '.length', lock=True)
        node[0] = cmds.rename(result, 'polyChamfer#')
    if deleteFace == 1:
        getFaces()
        cmds.delete()
    else:
        cmds.DeleteVertex()
    return node


def getNgons(q=False):
    '''Selects Ngons in Selection

    Args:
        q(boolean): if true fucntion returns the selection.

    Return:
        result(list): the NGons in selection
    '''
    cmds.selectMode(co=True)
    cmds.selectType(smp=False, sme=True, smf=False, smu=False, pv=False, pe=True, pf=False, puv=False)
    cmds.polySelectConstraint(mode=3, t=0x0008, size=3)
    cmds.polySelectConstraint(disable=True)
    nPolys = cmds.polyEvaluate(faceComponent=True)
    print >> sys.stderr, str(nPolys) + ' N-Gon(s) Selected.',

    if q:
        result = cmds.ls(sl=True, fl=True)
        return result


def getTris(q=False):
    '''
    Selects Triangles in Selection

    Args:
        q(boolean): if true function returns the selection.

    Return:
        result(list): the triangles in the selection
    '''
    cmds.selectMode(co=True)
    cmds.selectType(smp=False, sme=True, smf=False, smu=False, pv=False, pe=True, pf=False, puv=False)
    cmds.polySelectConstraint(mode=3, t=0x0008, size=1)
    cmds.polySelectConstraint(disable=True)
    nPolys = cmds.polyEvaluate(faceComponent=True)
    print >> sys.stderr, str(nPolys) + ' Triangles(s) Selected.',

    if q:
        result = cmds.ls(sl=True, fl=True)
        return result


def getComponetsCenter(sel):
    '''
    get the average postion of multiple componets

    Args:
        sel(list): list of componets to operate on.

        Return:
            averaged xyz coords
    '''
    vecSum = [0, 0, 0]
    for i in sel:
        vecSum[0] = vecSum[0] + cmds.pointPosition(i)[0]
        vecSum[1] = vecSum[1] + cmds.pointPosition(i)[1]
        vecSum[2] = vecSum[2] + cmds.pointPosition(i)[2]
    vecSum[0] = vecSum[0] / len(sel)
    vecSum[1] = vecSum[1] / len(sel)
    vecSum[2] = vecSum[2] / len(sel)
    return vecSum


def getCurrentCamera():
    '''
    gets the current maya viewport camera

    returns:
        cam(string): the current viewport camras name
    '''
    pan = cmds.getPanel(wf=True)
    cam = cmds.modelPanel(pan, q=True, camera=True)
    return cam


def setCurrentCamera(cam):
    '''
    Sets the current maya viewport camera.

    Args:
        cam(string): the camras name you want to set
    '''
    vpPanel = cmds.getPanel(wf=True)
    cmds.lookThru(vpPanel, cam)


def viewportSnap():
    '''
    Zbrush/Nvil like viewport snap
    '''
    camList = cmds.listCameras(o=True)

    if 'bottom' not in camList:
        cmds.duplicate('top', name='bottom')
        cmds.setAttr('bottom.translateY', -512)
        cmds.setAttr('bottom.rotateX', 90)

    if 'back' not in camList:
        cmds.duplicate('front', name='back')
        cmds.setAttr('back.translateZ', -512)
        cmds.setAttr('back.rotateY', 180)

    if 'left' not in camList:
        cmds.duplicate('side', name='left')
        cmds.setAttr('left.translateX', -512)
        cmds.setAttr('left.rotateY', -90)

    if getCurrentCamera() == 'persp':
        tm = cmds.xform('persp', q=True, ws=True, matrix=True)
        perspV = MVector(-tm[8], -tm[9], -tm[10])

        dotList = {}
        for view in camList:
            tm = cmds.xform(view, q=True, ws=True, matrix=True)
            tm = MVector(-tm[8], -tm[9], -tm[10])
            tm = perspV * tm
            dotList[view] = tm

        bv = max(dotList, key=dotList.get)
        setCurrentCamera(bv)
    else:
        setCurrentCamera('persp')


def getEdgeLength(sel):  # FIXME
    sel = cmds.filterExpand(sel, ex=1, sm=32)
    p = cmds.xform(sel, q=True, t=True, ws=True)
    raise Exception(p)
    length = math.sqrt(math.pow(p[0] - p[3], 2) + math.pow(p[1] - p[4], 2) + math.pow(p[2] - p[5], 2))
    return length


def distFromCam(sel):
    '''
    Gets objects distance from current camera, usefull for interactive tools with dynamic  mp's on attributes.

    Args:
        sel(string): name of object to work on.

    Returns: Distance between object in args and camera.
    '''
    cam = getCurrentCamera()
    # cam = 'persp'
    c = cmds.xform(cam, q=True, t=True, ws=True)
    s = cmds.xform(sel, q=True, t=True, ws=True)
    dist = math.sqrt(math.pow(c[0] - s[0], 2) + math.pow(c[1] - s[1], 2) + math.pow(c[2] - s[2], 2))
    return dist
