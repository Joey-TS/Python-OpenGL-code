from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

x = 0
y = 0

def plot_point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def first_egghalf(xc, yc, a, b):
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    for i in range(85, 271):
        y = b * math.sin(i * 3.14 / 180) + yc
        x = a * math.cos(i * 3.14 / 180) + xc
        glVertex2f(x, y)
    glEnd()
    glFlush()

def animate(timervalue):
    global x, y
    x -= 5  # Move the ellipse towards the left
    glutPostRedisplay()  # Trigger redraw
    glutTimerFunc(50, animate, 0)

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-500, 500, -500, 500)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    first_egghalf(x, y, 300, 200)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Animate Half Ellipse")
glutDisplayFunc(draw)
glutTimerFunc(0, animate, 0)
init()
glutMainLoop()
