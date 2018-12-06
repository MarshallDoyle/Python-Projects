#Python Pong Game 
#Based on the work of Christian Thompson, edited by Marshall Doyle
#Two Players: player one uses WASD: player two uses arrow keyes

import turtle

wn = turtle.Screen()
wn.title("Pong - Player1 uses WASD - Player2 uses Arrows")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Speed Control
ball_speed = 1
#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Speed of animation, 0 is fastest possible
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Speed of animation, 0 is fastest possible
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
	#dx & dy is the number that sets how many pixels on the screen the ball will travel every movement
	#Feel free to change dx & dy to work for your screen
ball.dx = 0.25
ball.dy = 0.25
balldx = ball.dx
balldy = ball.dy

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Functions
	#Functions for paddle_a
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

	#Functions for paddle_b
def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

#Keyboard Binding
wn.listen() #Tells the Program to expect keyboard input
wn.onkeypress(paddle_a_up, "w") #If the "w" key is pressed, then the paddle_a_up function will run
wn.onkeypress(paddle_a_down, "s") #If the "s" key is pressed, then the paddle_a_down function will run
wn.onkeypress(paddle_b_up, "Up") #If the "Up arrow" key is pressed, then the paddle_b_up function will run
wn.onkeypress(paddle_b_down, "Down") #If the "Down arrow" key is pressed, then the paddle_b_down function will run


#Loop runs while game is active
while True:
	wn.update()

	#Ball Movement
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		#Set ball.dx = 0.25 while retaining the positive/negative value
		if ball.dx > 0:
			ball.dx = balldx
		else:
			ball.dx = balldx*-1
		ball.goto(0, 0)
		ball.dx *= -1
		score_a +=1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	if ball.xcor() < -390:
		#Set ball.dx = 0.25 while retaining the positive/negative value
		if ball.dx > 0:
			ball.dx = balldx
		else:
			ball.dx = balldx*-1
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	#Paddle Collision
	if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
		ball.setx(340)
		ball.dx *= -1
		ball_speed += 0.1
		ball.dx *= ball_speed
		ball.dy *= ball_speed

	if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
		ball.setx(-340)
		ball.dx *= -1
		ball_speed += 0.1
		ball.dx *= ball_speed
		ball.dy *= ball_speed