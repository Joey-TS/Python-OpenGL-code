from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

theta=0
x=0

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-500,500,-500,500)

def drawline(x1,y1,x2,y2):
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

def bridge():
    glColor3f(1,1,1)
    drawline(-500,0,-100,0)
    drawline(500,0,100,0)
    drawbridge1()
    drawbridge2()
    glFlush()


def drawbridge1():
    global theta
    glColor3f(1,0,0)
    glLineWidth(4)
    glPushMatrix()
    glTranslate(-100,0,0)
    glRotatef(theta,0,0,1)
    drawline(100,0,0,0)
    glPopMatrix()

def drawbridge2():
    global theta
    glColor3f(1,0,1)
    glPushMatrix()
    glTranslate(100,0,0)
    glRotatef(-theta,0,0,1)
    drawline(-100,0,0,0)
    glPopMatrix()

def ship(tx,ty):
    glBegin(GL_POLYGON)
    glVertex(0+tx,0+ty)
    glVertex(40+tx,0+ty)
    glVertex(70+tx,30+ty)
    glVertex(-30+tx,30+ty)
    glEnd()
    glFlush()

def river():
    glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    glVertex(-1000,-900)
    glVertex(900,1000)
    glVertex(1000,900)
    glVertex(-900,-1000)
    glEnd()
    glFlush()
    
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    river()
    bridge()
    ship(-200+x,-200+x)
    

def animate(timervalue):
    global theta,x
    if theta<90:
        theta+=5
    if (x<600):
        x=x+10
        if (x>300):
            theta=theta-15
    ship(-200+x,-200+x)
    glutPostRedisplay()
    glutTimerFunc(50,animate,0)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000,1000)
glutInitWindowPosition(0,0)
glutCreateWindow(b"Ship")
glutDisplayFunc(lambda:draw())
glutTimerFunc(0,animate,0)
init()
glutMainLoop()
