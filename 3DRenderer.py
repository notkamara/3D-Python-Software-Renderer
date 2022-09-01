import pygame, math, threading, transform
from pygame.locals import *

width = 300
height = 300

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("3D Renderer")

clock = pygame.time.Clock()
gameExit = False

vertex1 = [0.0,1.0,2.0]
vertex2 = [1.0,-1.0,2.0]
vertex3 = [-1.0,-1.0,2.0]

fov = 90

scanBuffer = []

for y in range(0, height * 2):
    scanBuffer.append(0)

def scanConvertLine(v1, v2, ref):

    xStart = v1[0]
    xEnd = v2[0]
    
    yStart = v1[1]
    yEnd = v2[1]
    
    xDist = xEnd - xStart
    yDist = yEnd - yStart

    if yDist <= 0:
        return
    
    dX = float(xDist) / float(yDist)
    x = float(xStart)
    
    for i in range(int(yStart), int(yEnd)):
        scanBuffer[(i * 2) + ref] = x
        x += dX

def renderTriangle(v1, v2, v3):
    hWidth = width/2
    hHeight = height/2
    
    v1 = (((v1[0]/v1[2]) * hHeight) + hWidth, (-(v1[1]/v1[2]) * hHeight) + hHeight, v1[2])
    v2 = (((v2[0]/v2[2]) * hHeight) + hWidth, (-(v2[1]/v2[2]) * hHeight) + hHeight, v2[2])
    v3 = (((v3[0]/v3[2]) * hHeight) + hWidth, (-(v3[1]/v3[2]) * hHeight) + hHeight, v3[2])
    
    if v1[1] > v2[1]:
        temp = v1
        v1 = v2
        v2 = temp
    if v2[1] > v3[1]:
        temp = v1
        v1 = v3
        v3 = temp
    if v1[1] > v2[1]:
        temp = v1
        v1 = v2
        v2 = temp
    
    areaSign = ((v1[0] - v3[0]) * (v1[1] - v2[1])) - ((v1[0] - v2[0]) * (v1[1] - v3[1]))

    ref = 0

    if areaSign < 0:
        ref = 0
    else:
        ref = 1
    
    scanConvertLine(v1, v3, ref)
    scanConvertLine(v1, v2, 1 - ref)
    scanConvertLine(v2, v3, 1 - ref)

    for y in range(int(v1[1]), int(v3[1])):
        xStart = int(scanBuffer[y * 2])
        xEnd = int(scanBuffer[(y * 2) + 1])
        for x in range(int(xStart), int(xEnd)):
            screen.set_at((x, y), (255,255,255))
                          
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    vertex1 = transform.rotateY(vertex1, 1, (0,0,2))
    vertex2 = transform.rotateY(vertex2, 1, (0,0,2))
    vertex3 = transform.rotateY(vertex3, 1, (0,0,2))

    print vertex1 + vertex2 + vertex3

    screen.fill((0,0,0))
    renderTriangle(vertex1, vertex2, vertex3)
    pygame.display.update()
    clock.tick()
pygame.quit()
quit()

##        if event.type == KEYDOWN:
##            if event.key == K_UP:
##
##            elif event.key == K_DOWN:
##
##            elif event.key == K_LEFT:
##
##            elif event.key == K_RIGHT:
##
##        if event.type == KEYUP:
##            if event.key == K_UP:
##
##            elif event.key == K_DOWN:
##
##            elif event.key == K_LEFT:
##
##            elif event.key == K_RIGHT:
