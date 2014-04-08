import os
import pymel.core as pm
import sys

objPath = os.environ['APPDATA']
objPath = objPath + '/DigitalFossils/NVil/Media/Clipboard/ClipboardObj.obj'


def importObj():
    try:
        pm.importFile(objPath)
        sys.stderr.write('NvilClipboard Imported!')
    except:
        pm.warning('File Not Found!')


def exportObj(center=False):
    sel = pm.selected()
    if len(sel) == 0:
        pm.warning('Nothing is Selected!')
    else:
        if center:
            for obj in sel:
                oldLoc = obj.getRotatePivot()
                centerPiv(obj)
                pm.exportSelected(objPath, pr=True, typ='OBJexport', es=1, force=True, op="groups=1;ptgroups=1;materials=1;smoothing=1;normals=1")
                sys.stderr.write('NvilClipboard Exported!')
                obj.translateBy(oldLoc)
        else:
            pm.exportSelected(objPath, pr=True, typ='OBJexport', es=1, force=True, op="groups=1;ptgroups=1;materials=1;smoothing=1;normals=1")
            sys.stderr.write('NvilClipboard Exported!')


def centerPiv(obj):
    pm.select(obj)
    pm.makeIdentity(apply=True, t=True, r=True, s=True, n=False)
    pos = obj.getRotatePivot()
    obj.translate.set(-1 * pos)
