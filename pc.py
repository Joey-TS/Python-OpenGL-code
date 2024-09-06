# 104 Joseph

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

window_size = 800
border = 100
point_size = 5


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def point_code(x, y):
    return [1 if y > window_size - border else 0, 1 if y < border else 0, 1 if x > window_size - border else 0,
            1 if x < border else 0]

def perform_and(p1, p2):
    return [c1 and c2 for c1, c2 in zip(point_code(*p1), point_code(*p2))]

def perform_or(p1, p2):
    return [c1 or c2 for c1, c2 in zip(point_code(*p1), point_code(*p2))]

def check_line_visibility(p1, p2):
    if perform_or(p1, p2) == [0, 0, 0, 0]:
        return 1, "visible"
    elif perform_and(p1, p2) != [0, 0, 0, 0]:
        return 2, "invisible"
    else:
        return 3, "clipped"


def plot_line(p1, p2, color=(1, 0, 1)):
    glColor3f(*color)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(*p1)
    glVertex2f(*p2)
    glEnd()
    glFlush()


def plot_clipping_window():
    glColor3f(1, 1, 1)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    glVertex2f(border, border)
    glVertex2f(border, window_size - border)
    glVertex2f(window_size - border, window_size - border)
    glVertex2f(window_size - border, border)
    glEnd()

def point_code(x, y):
    return [1 if y > window_size - border else 0, 1 if y < border else 0, 1 if x > window_size - border else 0,
            1 if x < border else 0]

def get_clipped_point(point, m):
    code = point_code(*point)
    if code[-1] == 1:
        if code[0] == 1:
            point[1] = window_size - border
        elif code[1] == 1:
            point[1] = border
        else:
            point[1] = point[1] + m * (border - point[0])
        point[0] = border
        
    elif code[-2] == 1:
        if code[0] == 1:
            point[1] = window_size - border
        elif code[1] == 1:
            point[1] = border
        else:
            point[1] = point[1] + m * (window_size - border - point[0])
        point[0] = window_size - border
        
    elif code[0] == 1:
        if code[-1] == 1:
            point[0] = border
        elif code[-2] == 1:
            point[0] = window_size - border
        else:
            point[0] = point[0] + (window_size - border - point[1]) / m
        point[1] = window_size - border

    elif code[1] == 1:
        if code[-1] == 1:
            point[0] = border
        elif code[-2] == 1:
            point[0] = window_size - border
        else:
            point[0] = point[0] + (border - point[1]) / m
        point[1] = border


def slop(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def get_clipped_points(p1, p2):
    visibility, _ = check_line_visibility(p1, p2)
    if visibility == 3:
        m = slop(p1, p2)
        get_clipped_point(p1, m)
        get_clipped_point(p2, m)
    return p1, p2


def plot_clipped_line(p1, p2):
    plot_line(*get_clipped_points(p1, p2))


def display():
    gluOrtho2D(0, window_size, 0, window_size)
    glClear(GL_COLOR_BUFFER_BIT)
    plot_clipping_window()
    p1 = [window_size / 2, border / 2]
    p2 = [border / 2, window_size / 2]
    p3 = [window_size / 2, window_size - border / 2]
    p4 = [window_size - border / 2, window_size / 2]

    plot_clipped_polygon([p1, p2, p3, p4])
    plot_clipped_line(p1, p2)
    glFlush()

def plot_clipped_polygon(vertices):
    vertices.append(vertices[0])
    for i in range(len(vertices) - 1):
        glPointSize=7
        glColor3f(1,0,0)
        glBegin(GL_POINTS)
        glVertex2f(*vertices[i])
        glEnd()
        glFlush()
        print(vertices[i][:], vertices[i + 1][:])
        plot_line(vertices[i][:], vertices[i + 1][:], [0, 0, 1])
        plot_clipped_line(vertices[i][:], vertices[i + 1][:])

def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow(b"transformations")
    glutDisplayFunc(display)
    glutMainLoop()


main()
