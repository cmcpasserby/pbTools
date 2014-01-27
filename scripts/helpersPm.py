import math
import pymel.core as pm


def spherize():
    sel = pm.selected()
    if not sel:
        pm.warning('Nothing is Selected')
    verts = prepSelection(sel)
    points = [p.getPosition(space='world') for p in verts]
    center = getCenter(points)
    normals = [n.getNormal() for n in verts]
    normalPlane = averageVector(normals)

    pointsNew = [projectOrtho(center, normalPlane, p) for p in points]

    radius = getDist(center, pointsNew)
    for i in range(len(pointsNew)):
        pointsNew[i] = sphere(center, radius, pointsNew[i])

    for i in range(len(pointsNew)):
        pointsNew[i] = linePlaneInter(points[i], normals[i], pointsNew[i], normalPlane)

    for i in range(len(verts)):
        verts[i].setPosition(pointsNew[i], space='world')


def prepSelection(sel):
    verts = pm.filterExpand(sel, selectionMask=31)
    if verts:
        pm.polySelectConstraint(pp=3, type=0x0001)
        verts = pm.ls(sl=True, fl=True)
        return verts

    edge = pm.filterExpand(sel, selectionMask=32)
    if edge:
        verts = pm.polyListComponentConversion(edge, fromEdge=True, toVertex=True)
        return verts


def getCenter(points):
    pointSum = pm.dt.Point(0, 0, 0)
    for v in points:
        pointSum = pointSum + v
    return pointSum / len(points)


def averageVector(vecs):
    vecSum = pm.dt.Vector(0, 0, 0)
    for v in vecs:
        vecSum = vecSum + v
    vecSum = vecSum / len(vecs)
    return vecSum.normal()


def projectOrtho(ctr, pNrm, point):
    vec = point - ctr
    dist = vec * pNrm
    offset = pNrm * dist
    return point - offset


def getDist(ctr, nPoint):
    dist = 0
    for p in nPoint:
        dist += length(ctr, p)
    dist = dist / len(nPoint)
    return dist


def length(ctr, p):
    d = 0.0
    for i in range(len(ctr)):
        d += (ctr[i] - p[i]) * (ctr[i] - p[i])
    return math.sqrt(d)


def sphere(center, radius, point):
    vec = point - center
    vec.normalize()
    vec = vec * radius
    return vec + center


def linePlaneInter(points, normals, pointsNew, normalPlane):
    pointsNew = pointsNew - (normalPlane * 10000000)
    t = ((points - pointsNew) * normals) / (normals * normalPlane)
    intersection = (normalPlane * t) + pointsNew
    return intersection
