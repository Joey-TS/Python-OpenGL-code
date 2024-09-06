from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global vcodes, polygon_vertices, clipped_polygon
vcodes=[]
polygon_vertices=[]
clipped_polygon=[]


def code(x1,y1):
    code1=0000
    if (x1 < -150):
        code1+=1
    elif (x1 > 150):
        code1+=10
    if (y1 < -150):
        code1+=100
    elif (y1 > 150):
        code1+=1000
        
    vcodes.append(code1)

def draw_rectangle():
    glColor3f(1, 1, 1)  # Set color to white
    glLineWidth(2)     # Set line width to 2
    glBegin(GL_LINE_LOOP)
    length = 300
    breadth = 250
    # Calculate the coordinates of the four vertices of the rectangle
    x1, y1 = -length / 2, -breadth / 2
    x2, y2 = length / 2, -breadth / 2
    x3, y3 = length / 2, breadth / 2
    x4, y4 = -length / 2, breadth / 2
    # Draw the rectangle using a line loop
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def draw_polygon():
    num_vertices = int(input("Enter the number of vertices for the polygon: "))
    #polygon_vertices = []
    glColor3f(1, 0, 1)  # Set color to magenta
    glLineWidth(2)     # Set line width to 2
    glBegin(GL_LINE_LOOP)
    # Get input for each vertex
    for _ in range(num_vertices):
        x = int(input("Enter x-coordinate for vertex: "))
        y = int(input("Enter y-coordinate for vertex: "))
        glVertex2f(x, y)
        polygon_vertices.append((x, y))
        code(x,y)
    glEnd()

    return polygon_vertices

def clipping(num_vertices):
    vcodes.append(vcodes[0])
    polygon_vertices.append(polygon_vertices[0])
    j=0
    for i in range (1,num_vertices):
        code1 = vcodes[i-1]
        code2 = vcodes[i]
        v1=polygon_vertices[i-1]
        v2=polygon_vertices[i]
        if code1==0000:
            clipped_polygon.append(v1)
        if code2==0000:
            clipped_polygon.append(v2)
        if (code1/1000==1 and code2/1000==1):
            print("Line is completely outside the rectangle")
        elif (code1/100==1 and code2/100==1):
            print("Line is completely outside the rectangle")
        elif (code1%100==1 and code2%100==1):
            print("Line is completely outside the rectangle")
        elif (code1%100==10 and code2%100==10):
            print("Line is completely outside the rectangle")
        else:
            x1=v1[0]
            x2=v2[0]
            y1=v1[1]
            y2=v2[1]
            m=(y2-y1)/(x2-x1)
            if (x1 < -150):
                y1 = y1+ (-150 - x1)*m
                x1=-150
            if (x1 > 150):
                y1 = y1+ (150 - x1)*m
                x1=150
            if (y1 < -150):
                x1 = x1 + (-150 - y1)/m
                y1 = 150
            if (y1 > 150):
                x1 = x1 + (150 -y1)/m
                y1 = 150
            clipped_polygon.append((x1,y1))
    glColor3f(0, 1, 0)  # Set color to magenta
    glLineWidth(2)     # Set line width to 2
    glBegin(GL_LINE_LOOP)
    # Get input for each vertex
    for i in (clipped_polygon):
        glVertex2f(i[0], i[1])
    glEnd()
        
        

    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    gluOrtho2D(-500, 500, -500, 500)
    draw_rectangle()
    num_vertices = len(draw_polygon())
    clipping(num_vertices)
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"Polygon Clipping")
    glutDisplayFunc(display)
    glutMainLoop()

main()
