###################################################################################### 
#### Note this code has been developed and tested using Python version 3.9.5 in macOS
######################################################################################

import turtle
import random
import math

## Program Parameters
score = 0
game_over = False
playerspeed = 20
enemies = [] ## Create an empty list of enemies
enemy_colors = ['red', 'green', 'blue', 'orange', 'gray']
enemyspeed = 100

bullet_width = 0.2
bullet_height = 0.5
bulletspeed = 12
delayB = 1

## Get user input for levels, Higher level => faster enemy movement and smaller enemy size 
level = turtle.textinput("Enter Level", "Levels is 1-5 (1 being easiest and 5 is hardest")

if level == "1":
    game_level = 1
    enemysize = 3.0
    number_of_enemies = random.randint(10, 15) ## Choose a number of enemies

    delayT   = 30
    x_shift = 2
    y_shift = 0.25
    collision_margin = 20

elif level == "2":
    game_level = 2
    enemysize = 2.5
    number_of_enemies = random.randint(12, 20) ## Choose a number of enemies

    delayT   = 25
    x_shift = 4
    y_shift = 0.5
    collision_margin = 17.5

elif level == "3":
    game_level = 3
    enemysize = 2.0
    number_of_enemies = random.randint(15, 25) ## Choose a number of enemies

    delayT   = 20
    x_shift = 6
    y_shift = 0.75
    collision_margin = 15

elif level == "4":
    game_level = 4
    enemysize = 1.5
    number_of_enemies = random.randint(18, 30) ## Choose a number of enemies

    delayT   = 15
    x_shift = 8
    y_shift = 1.0
    collision_margin = 12.5

elif level == "5":
    game_level = 5
    enemysize = 1.0
    number_of_enemies = random.randint(20, 35) ## Choose a number of enemies

    delayT   = 10
    x_shift = 10
    y_shift = 1.25
    collision_margin = 10

else: ## Default level is level 1
    game_level = 1
    enemysize = 3.0
    number_of_enemies = random.randint(10, 15) ## Choose a number of enemies

    delayT  = 30
    x_shift = 2
    y_shift = 0.25
    collision_margin = 20

## Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.delay(0)
screen.tracer(5,0)

## Draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()         

## Create player turtle
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.shapesize(2)
player.penup()
player.speed(0)
player.setposition(0, -200)
player.setheading(90)      

## Create the bullet
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(bullet_width, bullet_height)
bullet.goto(0,0)

bullet_in_motion = False       

## Print the score
scoreturtle = turtle.Turtle()
scoreturtle.speed(0)
scoreturtle.color("white")
scoreturtle.penup()
scoreturtle.setposition(-304, 300)
scoreturtle.write("Score:", align="left", font=("Arial", 25, "normal"))
scoreturtle.hideturtle()

## Print the game level
levelturtle = turtle.Turtle()
levelturtle.speed(0)
levelturtle.color("white")
levelturtle.penup()
levelturtle.setposition(210, 300)
level_print =  "Level: %s" %game_level
levelturtle.write(level_print, align="left", font=("Arial", 25, "normal"))
levelturtle.hideturtle()

## Game Over Turtle
gameOverTurtle = turtle.Turtle()
gameOverTurtle.color("white")
gameOverTurtle.penup()
gameOverTurtle.speed(0)
gameOverTurtle.goto(0,0)
gameOverTurtle.hideturtle()

## Creating the Enemies and appending the enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color(enemy_colors[random.randint(0,4)])
    enemy.shape("turtle")
    enemy.penup()
    enemy.speed(0)
    enemy.shapesize(enemysize)
    x = random.randint(-200, 200)
    y = random.randint(100, 200)
    enemy.setposition(x, y)

def move_enemies():
    global game_over

    for enemy in enemies:
        x = enemy.xcor() + x_shift * random.randint(-3,3)
        if x > 275:
            x = 275
        elif x < -275:
            x = -275
        y = enemy.ycor() - y_shift 
        if y < -200:
            game_over = True
            gameOverTurtle.write("Game Over! \n You've been invaded!", align="center", font=("Arial", 35, "normal"))
            gameOverTurtle.showturtle()
        enemy.setposition(x, y)
        
    if game_over == False:
        screen.ontimer(move_enemies, delayT)

## Move the player left and right##
def move_left():

    if game_over == False:
        x = player.xcor()
        x -= playerspeed
        if x < -280:
          x = - 280
        player.setx(x)
    
def move_right():

    if game_over == False:
        x = player.xcor()
        x += playerspeed
        if x > 280:
            x = 280
        player.setx(x)

## Fire the bullet
def check_collision():
    global score
    global collision
    global bullet_in_motion

    i = 0
    collision = False

    for enemy in enemies:
        if collision == False :
            if  (math.sqrt(math.pow((bullet.xcor() - enemy.xcor()),2) + math.pow((bullet.ycor() - enemy.ycor()),2)) < collision_margin):
                collision = True
            
        if collision == True:
            score = score + 1
            enemy.hideturtle()
            enemies.pop(i)
            bullet.hideturtle()
            bullet_in_motion = False

            ## Update the score
            score_now =  "Score: %s" %score
            scoreturtle.clear()
            scoreturtle.write(score_now, False, align="left", font=("Arial", 25, "normal"))
 
            if len(enemies) == 0:
                game_over = True
                gameOverTurtle.write("All Enemies Invaded \n         You Won!", align="center", font=("Arial", 35, "normal"))
                gameOverTurtle.showturtle()
            
            break
        
        i = i + 1 

def move_bullet():
    global bullet_in_motion
    global collision
    global game_over

    if bullet_in_motion == True:
        x = bullet.xcor()
        y = bullet.ycor()
        y = y + bulletspeed   
        bullet.goto(x, y)
        check_collision()

    if bullet.ycor() > 290 :
        bullet.hideturtle()
        bullet_in_motion = False
    elif collision == False and game_over == False:
        screen.ontimer(move_bullet, delayB)

def fire_bullet():
    global bullet_in_motion
    global game_over

    ## Move bullet to just above the player
    if bullet_in_motion == False and game_over == False:
        bullet_in_motion = True
        x = player.xcor()
        y = player.ycor() + bulletspeed
        bullet.goto(x, y)
        bullet.showturtle()
        move_bullet()

## Main loop starts here
screen.listen()
screen.onkey(move_left,   "Left")
screen.onkey(move_left,   "L")
screen.onkey(move_left,   "l")
screen.onkey(move_right,  "Right")
screen.onkey(move_right,   "R")
screen.onkey(move_right,   "r")
screen.onkey(fire_bullet, "Up")
screen.onkey(fire_bullet, "U")
screen.onkey(fire_bullet, "u")

move_enemies()

turtle.update()

turtle.mainloop()