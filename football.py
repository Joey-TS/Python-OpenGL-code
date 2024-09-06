import math
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x=-200
y=0
leg1_angle=0
leg2_angle=0
ball_velocity=[5,13]
ball_position=[-200+20/2,0-20*2]

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-500,500,-500,500)
	glPointSize(5)
	glLineWidth(5)

def draw_circle(x,y,radius):
	num_seg=100
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y)
	for i in range(num_seg+1):
		theta=(2*math.pi*i)/num_seg
		xi=x+radius*math.cos(theta)
		yi=y+radius*math.sin(theta)
		glVertex2f(xi,yi)
	glEnd()

def draw_line(x1,y1,x2,y2):
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()

def animated_leg():
	global x,y,leg_angle
	glPushMatrix()
	glTranslatef(x,y,0)
	glRotatef(leg1_angle,0,0,1)
	draw_line(0,0,0-20,0-20*2)
	glPopMatrix()

def animated_leg2():
	global x,y,leg2_angle
	glPushMatrix()
	glTranslatef(x+200,y,0)
	glRotatef(leg2_angle,0,0,1)
	draw_line(0,0,0-20,0-20*2)
	glPopMatrix()

def goalpost():
	glBegin(GL_LINE_STRIP)
	glVertex2f(125,-40)
	glVertex2f(125,30)
	glVertex2f(145,30)
	glVertex2f(165,-40)
	glEnd()

def draw_stickman():
	
	global x,y,leg_angle
	glClear(GL_COLOR_BUFFER_BIT)
	#draw head
	head_radius=10
	draw_circle(x,y+20+head_radius,head_radius)
	#draw torso
	draw_line(x,y+20,x,y)
	#draw arms
	draw_line(x,y+20,x-20,y+20/2)
	draw_line(x,y+20,x+20,y+20/2)
	#draw legs
	animated_leg()
	draw_line(x,y,x+20,y-20*2)
	#draw ball
	draw_ball()
	
	
	#draw head
	head_radius=10
	draw_circle(x+200,y+20+head_radius,head_radius)
	#draw torso
	draw_line(x+200,y+20,x+200,y)
	#draw arms
	draw_line(x+200,y+20,x-20+200,y+20/2)
	draw_line(x+200,y+20,x+20+200,y+20/2)
	#draw legs
	animated_leg2()
	draw_line(x+200,y,x+20+200,y-20*2)
	
	#draw goalpost
	goalpost()
	
	glFlush()
	
def draw_ball():
	global leg1_angle,ball_position,ball_velocity
	draw_circle(ball_position[0],ball_position[1],20/4)
	
def animate(timervalue):
	global leg1_angle,ball_position
	#rotate leg
	leg1_angle+=10
	if leg1_angle>120:
		leg1_angle=120
	animate_ball_path()
	glutPostRedisplay()
	glutTimerFunc(50,animate,0)
	
def animate_ball_path():
	global ball_position,leg2_angle,ball_velocity
	if ball_position[0]<5:
		ball_position[0]+=4
	if ball_position[0]>=5:
		leg2_angle+=10
		if leg2_angle>120:
			leg2_angle=120
		if (ball_position[0]>=130):
			ball_position[0]=ball_position[0]
			ball_position[1]=ball_position[1]
		elif (ball_position[0]>=5):
			ball_position[0]+=ball_velocity[0]/2
			ball_position[1]+=ball_velocity[1]/2
			ball_velocity[1]-=1/2
		
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(1000,1000)
	glutInitWindowPosition(0,0)
	glutCreateWindow(b"Football")
	glutDisplayFunc(lambda:draw_stickman())
	glutTimerFunc(0,animate,0)
	init()
	glutMainLoop()
main()


#python3 football.py
