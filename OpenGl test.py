import math
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-300,300,-300,300)

def plot():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,1)
    glLineWidth(2)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    for i in range(0,361,1):
        glVertex2f(50*math.cos(math.pi*i/180),50*math.sin(math.pi*i/180))
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(600,0)
    glutCreateWindow(b"Sample")
    glutDisplayFunc(lambda:plot())
    init()
    glutMainLoop()

main()
