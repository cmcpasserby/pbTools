from maya.OpenMaya import MVector
import maya.cmds as cmds


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
