from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-500,500,-500,500)

def display(xc,yc,rx,ry):
    ellipse(xc,yc,rx,ry)

def ellipse(xc,yc,rx,ry):
    x,y=0,ry
    p=(ry**2)-(rx**2)*ry+(1/4)*(rx**2)
    plot(x,y,xc,yc)
    while (2*(ry**2)*x<=2*(rx**2)*y):
        if (p<0):
            x=x+1
            plot(x,y,xc,yc)
            p=p+2*(ry**2)*x+(ry**2)
        else:
            x=x+1
            y=y-1
            plot(x,y,xc,yc)
            p=p+2*(ry**2)*x+(ry**2)-2*(rx**2)*y
    while (y>0):
        p=(ry**2)*(x+0.5)**2+(rx**2)*(y-1)**2-(rx**2)*(ry**2)
        if p>0: 
            y=y-1
            plot(x,y,xc,yc)
            p=p-2*(rx**2)*y+(rx**2)
        else:
            x=x+1
            y=y-1
            plot(x,y,xc,yc)
            p=p+2*(ry**2)*x-2*(rx**2)*y+(rx**2)
            
def plot(x,y,xc,yc):
    glColor3f(0.2,0.6,0.8)
    glBegin(GL_POINTS)
    glVertex2f((xc + x) , (yc + y))
    glVertex2f((xc + x) , (yc - y))
    glVertex2f((xc - x) , (yc + y))
    glVertex2f((xc - x) , (yc - y))
    glEnd()
    glFlush()

def main():
    xc=int(input("Enter center x = "))
    yc=int(input("Enter center y = "))
    rx=int(input("Enter radius rx : "))
    ry=int(input("Enter radius ry : "))
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(1000,1000)
    glutCreateWindow(b"ellipse")
    glutDisplayFunc(lambda:display(xc,yc,rx,ry))
    init()
    glutMainLoop()
    
main()
