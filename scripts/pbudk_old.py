import maya.cmds as cmds
import maya.mel as mel
import pbTools.helpers as pbh


#main  function  builds window and UI
def pbUDKUI():

    versionNumber = " v1.02"
    title = "pbUDK"

    #deletes main window if it already exists
    if cmds.window("pbUDKWin", exists=True):
        cmds.deleteUI("pbUDKWin")

    #set up main window
    cmds.window("pbUDKWin", title=title + versionNumber, iconName=title + versionNumber, mb=True, mbv=True, mnb=False, mxb=False, nm=2, sizeable=False)

    #main window column
    cmds.columnLayout("BaseUIcolumn")

    #set defualt loc variables
    fbxbasepath = cmds.workspace(q=True, rd=True) + "data/"
    print fbxbasepath
    t3dbasepath = cmds.workspace(q=True, rd=True) + "data/UDKexport.t3d"

    #Mesh Reference
    cmds.frameLayout('referenceSettings', label="UDK Reference", collapsable=True, cl=False, bs="out", w=506, mh=10, p="BaseUIcolumn")
    cmds.columnLayout("RefUIcolumn")
    cmds.text(label="Reference:", align="left")
    cmds.textField('ReferenceLoc', w=500)
    cmds.rowColumnLayout(nc=2, cw=[(1, 250), (2, 250)], p="RefUIcolumn")
    cmds.button(h=30, label="Add Reference", c=lambda z: Add_Tag())
    cmds.button(h=30, label="Remove Reference", c=lambda z: Remove_Tag())

    #Mesh Export
    cmds.frameLayout('ExportMeshFL', label="Export Meshes (.FBX)", collapsable=True, cl=False, bs="out", w=506, mh=10, p="BaseUIcolumn")
    cmds.columnLayout("MeshUIColumn")
    cmds.text(label="Export Dirctory:", align="left")
    cmds.rowColumnLayout(nc=2, cw=[(1, 468), (2, 32)], p="MeshUIColumn")
    cmds.textField('fbxexportdir', text=fbxbasepath)
    cmds.button(h=20, label="...", c=lambda z: fbxPathset())
    cmds.button(h=30, label="Export Meshes", c=lambda z: UDKexport(), p="MeshUIColumn", w=500)

    #Tranformation Export
    cmds.frameLayout('ExportTranformationsFL', label="Export Tranformations (.T3D)", collapsable=True, cl=False, bs="out", w=506, mh=10, p="BaseUIcolumn")
    cmds.columnLayout("TranUIColumn")
    cmds.text(label="Export Dirctory:", align="left")
    cmds.rowColumnLayout(nc=2, cw=[(1, 468), (2, 32)], p="TranUIColumn")
    cmds.textField('t3dexportdir', text=t3dbasepath)
    cmds.button(h=20, label="...", c=lambda z: t3dPathset())
    cmds.text(label="UDK Map Name:", align="left", p="TranUIColumn")
    cmds.textField('udkmapname', text="UDK Map Name", p="TranUIColumn", w=500)
    cmds.button(h=30, label="Export Level", c=lambda z: ExportToT3D(), p="TranUIColumn", w=500)

    #Render window
    cmds.showWindow()


def t3dPathset():
    t3dbasepath = cmds.workspace(q=True, rd=True) + "data/UDKexport.t3d"
    filters = "Unreal Text (*.t3d)"
    t3dEPath = cmds.fileDialog2(dir=t3dbasepath, fm=0, ff=filters, cap="Set T3D Location")
    cmds.textField('t3dexportdir', e=True, fi=str(t3dEPath[0]))


def fbxPathset():
    fbxbasepath = cmds.workspace(q=True, rd=True) + "data/"
    fbxEPath = cmds.fileDialog2(dir=fbxbasepath, fm=3, okc="Select Folder", cap="Select Export Folder")
    cmds.textField('fbxexportdir', e=True, fi=str(fbxEPath[0] + '\\'))


#Add Reference
def Add_Tag():
    sel = cmds.ls(sl=True)
    if len(sel) >= 1:
        for item in sel:
            if  pbh.attributeExists('T3DTag', item):
                msg = "Attribute already exists on this object: " + item + ". Delete it first.\n"
                cmds.warning(msg)
            else:
                cmds.addAttr(item, ln="T3DTag", nn="T3D Tag", dt="string")
                tag = cmds.textField('ReferenceLoc', query=True, text=True)
                cmds.setAttr(item + ".T3DTag", tag, type="string")

                cmds.addAttr(item, ln="ExcludeFromExport", nn="Exclude From Export", at="bool")

                msg = "T3D tag [" + tag + "] added on object [" + item + "]\n"
                print msg,
    else:
        cmds.warning("Select at least one polygon object!")


#Remove Reference
def Remove_Tag():
    sel = cmds.ls(sl=True)
    if len(sel) >= 1:
        for item in sel:
            if  pbh.attributeExists('T3DTag', item):
                cmds.deleteAttr(item, at="T3DTag")
                cmds.deleteAttr(item, at="ExcludeFromExport")
                msg = "T3D reference removed on object [" + item + "]\n"
                cmds.warning(msg)
            else:
                msg = "There is no reference to be removed on this object: " + item + "\n"
                cmds.warning(msg)
    else:
        cmds.warning("Select at least one polygon object!")


#Export Mesh To FBX
def doexport(selExport):
    extension = ".fbx"
    FBXPath = cmds.textField('fbxexportdir', query=True, fi=True)
    ExportPath = (FBXPath + selExport + extension)
    cmds.select(selExport)
    mel.eval('FBXExport -f "' + ExportPath + '" -s;')
    # print ExportPath


def UDKexport():
    selection = cmds.ls(sl=True)
    bCenterPiv = "True"
    presetpath = cmds.internalVar(usd=True) + "UDK-FBX.fbxexportpreset"
    mel.eval('FBXLoadExportPresetFile -f "' + presetpath + '";')
    selsize = len(selection)

    if selsize == 0:
        cmds.warning("Nothing is Selected!")
    elif bCenterPiv == "True":
        for thisobj in selection:
            cmds.select(thisobj)
            OrginalLoc = cmds.xform(q=True, piv=True, ws=True)
            cmds.move(0, 0, 0, thisobj, a=True)
            doexport(thisobj)
            cmds.move(OrginalLoc[0], OrginalLoc[1], OrginalLoc[2], thisobj, a=True)

    else:
        for thisobj in selection:
            cmds.select(thisobj)
            doexport(thisobj)


# Export Tranformations To t3dpath
def ExportToT3D():
    sel = cmds.ls(sl=True)
    errorLog = ""

    if len(sel) > 0:
        #Export Paths
        t3dpath = cmds.textField('t3dexportdir', query=True, fi=True)
        mapname = cmds.textField('udkmapname', query=True, text=True)

        #Create .t3d file
        T3D_Text = open(t3dpath, "w")

        #t3d header
        T3D_Text.write("Begin Map Name=" + mapname + "\n")
        T3D_Text.write("  Begin Level Name=PersistentLevel\n")

        for count in range(len(sel)):
            if pbh.attributeExists('T3DTag', sel[count]):
                if not cmds.getAttr(sel[count] + ".ExcludeFromExport"):
                    #change rotation xyz to xzy
                    cmds.xform(sel[count], p=True, roo='xzy')

                    #array to File
                    tmp = sel[count]
                    refTag = cmds.getAttr(tmp + ".T3DTag")
                    dataT = cmds.xform(sel[count], query=True, t=True)
                    dataR = cmds.xform(sel[count], query=True, ro=True)
                    dataS = cmds.xform(sel[count], query=True, s=True)
                    #get ViewLayerName
                    #vlayer = #FIXME

                    dataR[0] *= 182.04444444444444444444444444444
                    dataR[1] *= -182.04444444444444444444444444444
                    dataR[2] *= 182.04444444444444444444444444444

                    T3D_Text.write("    Begin Actor Class=StaticMeshActor Name=StaticMeshActor_")
                    T3D_Text.write(str(count))
                    T3D_Text.write(" Archetype=StaticMeshActor'Engine.Default__StaticMeshActor'")
                    T3D_Text.write("\n        Begin Object Class=StaticMeshComponent Name=StaticMeshComponent0 Archetype=StaticMeshComponent'Engine.Default__StaticMeshActor:StaticMeshComponent0'\n")
                    T3D_Text.write("        StaticMesh=" + refTag + "\n")
                    T3D_Text.write("        End Object\n")

                    #Write Translation
                    T3D_Text.write("        Location=(X=")
                    T3D_Text.write(str(dataT[0]))
                    T3D_Text.write(",Y=")
                    T3D_Text.write(str(dataT[2]))
                    T3D_Text.write(",Z=")
                    T3D_Text.write(str(dataT[1]))
                    T3D_Text.write(")\n")

                    #Write Rotation
                    T3D_Text.write("        Rotation=(Roll=")
                    T3D_Text.write(str(int(dataR[0])))
                    T3D_Text.write(",Pitch=")
                    T3D_Text.write(str(int(dataR[2])))
                    T3D_Text.write(",Yaw=")
                    T3D_Text.write(str(int(dataR[1])))
                    T3D_Text.write(")\n")

                    #Write Scale
                    T3D_Text.write("        DrawScale3d=(X=")
                    T3D_Text.write(str(dataS[0]))
                    T3D_Text.write(",Y=")
                    T3D_Text.write(str(dataS[2]))
                    T3D_Text.write(",Z=")
                    T3D_Text.write(str(dataS[1]))
                    T3D_Text.write(")\n")

                    #Tag
                    T3D_Text.write("        Tag=\"PBComponent\"\n")

                    #Layer
                    #T3D_Text.write( "        Layer="#FIXME )

                    #End Actor
                    T3D_Text.write("    End Actor\n")

                    cmds.xform(sel[count], p=True, roo='xyz')

            else:
                errorLog += "\nFailed to Export " + sel[count] + "! No References Found."

        #Write File Footer
        T3D_Text.write("  End Level\n")
        T3D_Text.write("End Map\n")

        #write Error log if any
        if errorLog == "":
            print("\nExport Successful!", )

        else:
            print ("\nWarning: " + errorLog + "\n")
            print ("\nExport compleated with errors! Check Log!")
        T3D_Text.close()

    else:
        cmds.error("No Object Selected!")
