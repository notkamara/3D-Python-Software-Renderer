import math

def rotateX(point, rot, pointOfRot):
    prX, prY, prZ = pointOfRot
    x, y, z = point

    y -= prY
    z -= prZ
    
    newY = (y * math.cos((rot * math.pi)/180))-(z * math.sin((rot * math.pi)/180))
    newZ = (y * math.sin((rot * math.pi)/180))+(z * math.cos((rot * math.pi)/180))
    
    newPoint = (x, newY + prY, newZ + prZ)
    return newPoint

def rotateY(point, rot, pointOfRot):
    prX, prY, prZ = pointOfRot
    x, y, z = point

    x -= prX
    z -= prZ
    
    newX = (z * math.sin((rot * math.pi)/180))+(x * math.cos((rot * math.pi)/180))
    newZ = (z * math.cos((rot * math.pi)/180))-(x * math.sin((rot * math.pi)/180))
    
    newPoint = (newX + prX, y, newZ + prZ)
    return newPoint

def rotateZ(point, rot, pointOfRot):
    prX, prY, prZ = pointOfRot
    x, y, z = point

    x -= prX
    y -= prY
    
    newX = (x * math.cos((rot * math.pi)/180))-(y * math.sin((rot * math.pi)/180))
    newY = (x * math.sin((rot * math.pi)/180))+(y * math.cos((rot * math.pi)/180))

    newPoint = (newX + prX, newY + prY, z)
    return newPoint

def translate(point, translation):
    newX, newY, newZ = point
    x, y, z = translation

    newX += x
    newY += y
    newZ += z

    newPoint = (newX, newY, newZ)
    return newPoint
