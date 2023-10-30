import turtle
import random

## Some program parameters
score    = 0
moveX    = 25
moveYg   = 10
moveY    = 50
delayT   = 50
gap      = 250
barwidth = 50

maxX     = 1000
maxY     = 1000
birdX    = -200
startX1  = 100
startX2  = 400
endX     = -300
scoreX   = -400
scoreY   = 200

myturtle    = turtle.Turtle()
myupbar1    = turtle.Turtle()
mydownbar1  = turtle.Turtle()
myupbar2    = turtle.Turtle()
mydownbar2  = turtle.Turtle()
scoreturtle = turtle.Pen()
msgturtle   = turtle.Pen()

## Set the screen
myscreen = turtle.Screen() 
myscreen.setup(maxX, maxY)
turtle.Screen().bgcolor("blue")
myscreen.title("Flappy Bird")

## Configure the turtle bird
myturtle.pensize(5)
myturtle.penup()
myturtle.shape('turtle')
myturtle.shapesize(2)
myturtle.speed(0)
myturtle.goto(birdX,0)

## Configure the up bar
myupbar1.color('black')
myupbar1.pensize(5)
myupbar1.speed(0)
myupbar1.penup()
myupbar2.color('black')
myupbar2.pensize(5)
myupbar2.speed(0)
myupbar2.penup()

## Configure the down bar
mydownbar1.color('black')
mydownbar1.pensize(5)
mydownbar1.speed(0)
mydownbar1.penup()
mydownbar2.color('black')
mydownbar2.pensize(5)
mydownbar2.speed(0)
mydownbar2.penup()

## Configure the score turtle
scoreturtle.color('black')
scoreturtle.pensize(5)
scoreturtle.penup()
scoreturtle.shape('turtle')
scoreturtle.shapesize(2)
scoreturtle.speed(0)
scoreturtle.goto(0,0)
scoreturtle.hideturtle()

## Configure the msg turtle
msgturtle.color('black')
msgturtle.pensize(5)
msgturtle.penup()
msgturtle.shape('turtle')
msgturtle.shapesize(2)
msgturtle.speed(0)
msgturtle.goto(0,0)
msgturtle.hideturtle()

## Draw the bar
def drawbar():
    global xbox1
    global xbox2
    global height1
    global height2
    global score

    myupbar1.clear()
    mydownbar1.clear()
    myupbar2.clear()
    mydownbar2.clear()

    if xbox1 == endX :
        score = score + 1
        height1 = random.randint(maxY * 0.20, maxY * 0.70)
        xbox1   = startX2
    else :
        xbox1 = xbox1 - moveX

    if xbox2 == endX :
        score = score + 1
        height2 = random.randint(maxY * 0.20, maxY * 0.70)
        xbox2   = startX2
    else :
        xbox2 = xbox2 - moveX

    myupbar1.goto(xbox1,maxY/2)
    myupbar1.pendown()
    myupbar2.goto(xbox2,maxY/2)
    myupbar2.pendown()

    myupbar1.setheading(270)
    myupbar1.forward(height1)
    myupbar1.left(90)
    myupbar1.forward(barwidth)
    myupbar1.left(90)
    myupbar1.forward(height1)
    myupbar1.hideturtle()
    myupbar2.setheading(270)
    myupbar2.forward(height2)
    myupbar2.left(90)
    myupbar2.forward(barwidth)
    myupbar2.left(90)
    myupbar2.forward(height2)
    myupbar2.hideturtle()
     
    mydownbar1.goto(xbox1,-maxY/2)
    mydownbar1.pendown()
    mydownbar2.goto(xbox2,-maxY/2)
    mydownbar2.pendown()

    mydownbar1.setheading(90)
    mydownbar1.forward(maxY - gap - height1)
    mydownbar1.right(90)
    mydownbar1.forward(barwidth)
    mydownbar1.right(90)
    mydownbar1.forward(maxY - gap -height1)
    mydownbar1.hideturtle()
    mydownbar2.setheading(90)
    mydownbar2.forward(maxY - gap - height2)
    mydownbar2.right(90)
    mydownbar2.forward(barwidth)
    mydownbar2.right(90)
    mydownbar2.forward(maxY - gap -height2)
    mydownbar2.hideturtle()

    if collided == 0:
        myscreen.ontimer(drawbar, delayT)

def move():
    global collided
    xpos = myturtle.xcor()
    ypos = myturtle.ycor()
    ypos = ypos - moveYg   
    myturtle.goto(xpos, ypos)
    ### Call function again after delayT ms

    if collided == 0:
        myscreen.ontimer(move, delayT)

def Up():
    xpos = myturtle.xcor()
    ypos = myturtle.ycor()
    ypos = ypos + moveY    
    myturtle.goto(xpos, ypos)

def scoreBoard():
    global xbox1
    global xbox2
    global score
    global collided

    scoreturtle.goto(scoreX, scoreY)
    scoreturtle.pendown()
    scoreturtle.clear()
    scoreturtle.penup()
    scoreturtle.goto(scoreX -50, scoreY)
    scoreturtle.hideturtle()
    scoreturtle.pendown()
    scoreturtle.write("score:", align="center", font=("Arial", 25, "normal"))
    scoreturtle.hideturtle()
    scoreturtle.penup()
    scoreturtle.goto(scoreX, scoreY)
    scoreturtle.pendown()
    scoreturtle.write(score, align="center", font=("Arial", 20, "normal"))
    scoreturtle.hideturtle()
    scoreturtle.penup()

    if collided == 0:
        myscreen.ontimer(scoreBoard, delayT)

def birdCollision():
    global xbox1
    global xbox2
    global height1
    global height2
    global collided

    if myturtle.xcor() == xbox1:
        #If Bird collides bar 1
        if myturtle.ycor() > (maxY/2 - height1) or myturtle.ycor() < (maxY/2 - height1 - gap):
            collided = 1

    if myturtle.xcor() == xbox2:
        #If Bird collides bar 2
        if myturtle.ycor() > (maxY/2 - height2) or myturtle.ycor() < (maxY/2 - height2 - gap):
            collided = 1

    if collided == 1:
        myturtle.goto(0, -maxY/2)
        msgturtle.penup()
        msgturtle.write("Game Over !!", align="center", font=("Arial", 20, "normal"))
    else:
        myscreen.ontimer(birdCollision, delayT)

# Main Program
xbox1 = startX1
height1 = random.randint(maxY * 0.20, maxY * 0.70)

xbox2 = startX2
height2 = random.randint(maxY * 0.20, maxY * 0.70)

score = 0
collided = 0

turtle.listen()
turtle.onkey(Up,    'Up')

move()
drawbar()
scoreBoard()
birdCollision()

turtle.mainloop()