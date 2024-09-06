from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-500,500,-500,500)
    
def display(xc,yc,r):
    circle(xc,yc,r)
    
def circle(xc,yc,r):
    x,y=0,r
    p=1-r
    plot(x,y,xc,yc)
    while (x<=y):
        if p<0:
            x=x+1
            p+=2*x+1
            plot(x,y,xc,yc)
        else:
            x=x+1
            y=y-1
            p+=2*x-2*y+1
            plot(x,y,xc,yc)
            
def plot(x,y,xc,yc):
    glColor3f(0.2,0.6,0.8)
    glBegin(GL_POINTS)
    glVertex2f((xc + x) , (yc + y))
    glVertex2f((xc + x) , (yc - y))
    glVertex2f((xc - x) , (yc + y))
    glVertex2f((xc - x) , (yc - y))
    glVertex2f((xc + y) , (yc + x))
    glVertex2f((xc + y) , (yc - x))
    glVertex2f((xc - y) , (yc + x))
    glVertex2f((xc - y) , (yc - x))
    glEnd()
    glFlush()
    

    
def main():
    xc=int(input("Enter center x = "))
    yc=int(input("Enter center y = "))
    r=int(input("Enter radius : "))
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(1000,1000)
    glutCreateWindow(b"DDA")
    glutDisplayFunc(lambda:display(xc,yc,r))
    init()
    glutMainLoop()

main()
