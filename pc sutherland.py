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
    draw_line(n)
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

def draw_line():
    global wx_min, wy_min, wx_max, wy_max
    code1=0000
    code2=0000
    
    x1 = float(input("Enter the starting X coordinate: "))
    y1 = float(input("Enter the starting Y coordinate: "))
    x2 = float(input("Enter the ending X coordinate: "))
    y2 = float(input("Enter the ending Y coordinate: "))
    
    if (x1 < -150):
        code1+=1
    elif (x1 > 150):
        code1+=10
    if (y1 < -150):
        code1+=100
    elif (y1 > 150):
        code1+=1000
        
    if (x2 < -150):
        code2+=1
    elif (x2 > 150):
        code2+=10
    if (y2 < -150):
        code2+=100
    elif (y2 > 150):
        code2+=1000
        
    print(code1)
    print(code2)

    glColor3f(1, 1, 1) 
    glPointSize(5)
    glLineWidth(3)
    glBegin(GL_POINTS)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
    draw_line1(code1,x2,y2)

def draw_line1(code1,x1,y1):
    global wx_min, wy_min, wx_max, wy_max
    code2=0000

    x2 = float(input("Enter the ending X coordinate: "))
    y2 = float(input("Enter the ending Y coordinate: "))
    
    if (x1 < -150):
        code1+=1
    elif (x1 > 150):
        code1+=10
    if (y1 < -150):
        code1+=100
    elif (y1 > 150):
        code1+=1000
        
    if (x2 < -150):
        code2+=1
    elif (x2 > 150):
        code2+=10
    if (y2 < -150):
        code2+=100
    elif (y2 > 150):
        code2+=1000
        
    print(code1)
    print(code2)

    glColor3f(1, 1, 1) 
    glPointSize(5)
    glLineWidth(3)
    glBegin(GL_POINTS)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()


    
    if (code1/1000==1 and code2/1000==1):
        print("Line is completely outside the rectangle")
    elif (code1/100==1 and code2/100==1):
        print("Line is completely outside the rectangle")
    elif (code1%100==1 and code2%100==1):
        print("Line is completely outside the rectangle")
    elif (code1%100==10 and code2%100==10):
        print("Line is completely outside the rectangle")
    else:
        m=(y2-y1)/(x2-x1)
        if (x1 < -150):
            y1 = y1+ (-150 - x1)*m
            x1=-150
            plot_extra_point(x1,y1)
        if (x1 > 150):
            y1 = y1+ (150 - x1)*m
            x1=150
            plot_extra_point(x1,y1)
        if (y1 < -150):
            x1 = x1 + (-150 - y1)/m
            y1 = 150
            plot_extra_point(x1,y1)
        if (y1 > 150):
            x1 = x1 + (150 -y1)/m
            y1 = 150
            plot_extra_point(x1,y1)
            
        if (x2 < -150):
            y2 = y2+ (-150 - x2)*m
            x2=-150
            plot_extra_point(x2,y2)
        if (x2 > 150):
            y2 = y2+ (150 -x2)*m
            x2=150
            plot_extra_point(x2,y2)
        if (y2 < -150):
            x2 = x2 + (-150 - y2)/m
            y2 = -150
            plot_extra_point(x2,y2)
        if (y2 > 150):
            x2 = x2 + (150 - y2)/m
            y2 = 150
            plot_extra_point(x2,y2)
            
        glColor3f(1, 1, 1)
        glBegin(GL_LINES)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
        glEnd()
    
    

def main():
    num_vertices=int(input("Enter the number of vertices : "))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Sutherland line clipping")
    glutDisplayFunc(display(num_vertices))
    init()
    glutMainLoop()

main()
