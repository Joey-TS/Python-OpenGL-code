import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

wx_min=-150
wy_min=-150
wx_max=150
wy_max=150

def init():
    
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-500, 500, -500, 500)

def display():
    global wx_min, wy_min, wx_max, wy_max
    glClear(GL_COLOR_BUFFER_BIT)
    draw_line()
    draw_square()
    glFlush()

def draw_square():
    global wx_min, wy_min, wx_max, wy_max
    glColor3f(1,0,1)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(150, 150)
    glVertex2f(150, -150)
    glVertex2f(150, -150)
    glVertex2f(-150, -150)
    glVertex2f(-150, -150)
    glVertex2f(-150, 150)
    glVertex2f(-150, 150)
    glVertex2f(150, 150)
    glEnd()

def plot_extra_point(x,y):
    glColor3f(0,1,0)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def outside():
    for i+1 in sides_list:
        if (outside(i[0]) and !(outside(i[1]))):
            
            

def draw_line():
    global wx_min, wy_min, wx_max, wy_max
    
    
    
    

def main():
    sides = int(input("Enter number of sides of polygon : "))
    sides_list = []
    for i in range(0,sides):
        x = float(input(f"Enter Point {i+1} X corrdinate : "))
        y = float(input(f"Enter Point {i+1} Y corrdinate : "))
        sides_list.append([x,y])
    draw_sides=[]
    sides_list.append(sides_list[0])
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Sutherland line clipping")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()
