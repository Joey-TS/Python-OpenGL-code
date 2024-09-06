import math
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


x = -200
y = 0
leg_angle = 0

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-500,500,-500,500)

def draw_circle(x, y, radius):
    num_segments = 100
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(num_segments + 1):
        theta = (2.0 * math.pi * i) / num_segments
        xi = x + radius * math.cos(theta)
        yi = y + radius * math.sin(theta)
        glVertex2f(xi, yi)
    glEnd()

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def animated_leg():
    global x, y, leg_angle
    glPushMatrix()
    glTranslatef(x, y, 0)
    glRotatef(leg_angle, 0, 0, 1)
    draw_line(0, 0, 0 - 20, 0 - 20 * 2)
    glPopMatrix()

def draw_stickman():
    global x, y
    # Draw head
    head_radius = 20 / 2
    draw_circle(x, y + 20 + head_radius, head_radius)
    # Draw torso
    draw_line(x, y + 20, x, y)
    # Draw arms
    draw_line(x, y + 20, x - 20, y + 20 / 2)
    draw_line(x, y + 20, x + 20, y + 20 / 2)
    # Draw legs
    animated_leg()
    draw_line(x, y, x +20, y - 20 * 2)
    # Draw ball
    draw_ball_next_to_leg()
    glFlush()

def draw_ball_next_to_leg():
    global x, y
    # Calculate the position of the ball next to the east leg
    ball_x = x + 20/ 2 - 20
    ball_y = y - 20 * 2
    # Draw the ball
    draw_circle(ball_x, ball_y, 20 / 4)
    glFlush()

def animate(timer_value):
    global leg_angle
    # Rotate the leg 120 degrees anti-clockwise
    leg_angle += 2
    if leg_angle > 120:
        leg_angle = 120
    
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1000,1000)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b"Sample")
    glutDisplayFunc(lambda:draw_stickman())
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()

main()
