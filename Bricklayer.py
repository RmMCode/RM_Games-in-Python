import turtle

def drawRect(x, y, length, height):
    pointer.up()
    pointer.goto(x,y)
    pointer.begin_fill()
    pointer.down()
    pointer.goto(x+length, y)
    pointer.goto(x+length, y+height)
    pointer.goto(x, y+height)
    pointer.goto(x, y)
    pointer.up()
    pointer.end_fill()

def drawBrickWall():
    #put code here to draw a simple wall
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))
    brickWidth = int(input("Enter the brick width: "))
    brickHeight = int(input("Enter the brick height "))
    mortarWidth = int(input("Enter the mortar width: "))
    #this just draws one brick of the number of colsorrect size in the bottom right
    brick_start_x = 0
    brick_start_y = 0
    for i in range(0,rows):
        for j in range(0, cols):
            drawRect(brick_start_x, brick_start_y, brickWidth, brickHeight)
            brick_start_x += brickWidth + mortarWidth
        brick_start_x = 0
        brick_start_y += brickHeight + mortarWidth

def drawBrickWallOffset():
    #put code here to draw the fancy wall
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))
    brickWidth = int(input("Enter the brick width: "))
    brickHeight = int(input("Enter the brick height "))
    mortarWidth = int(input("Enter the mortar width: "))
    #this just draws one brick of the cmber of colsorrect size in the bottom right
    brick_start_x = 0
    brick_start_y = 0
    for i in range(0,rows):
        for j in range(0, cols+1):
            if (i % 2 == 0):
                if (j == cols):
                    drawRect(brick_start_x, brick_start_y, brickWidth/2, brickHeight)
                else :
                    drawRect(brick_start_x, brick_start_y, brickWidth-1, brickHeight)
            else:
                if (j == 0):
                        drawRect(brick_start_x, brick_start_y, brickWidth/2, brickHeight)
                else:
                    drawRect(brick_start_x - brickWidth/2, brick_start_y, brickWidth, brickHeight)
            brick_start_x += brickWidth + mortarWidth
        brick_start_x = 0
        brick_start_y += brickHeight + mortarWidth   

screen = turtle.Screen()
screen.screensize(400,400)
screen.setworldcoordinates(0,0,400,400)

pointer = turtle.Turtle()
pointer.up()
pointer.hideturtle()
pointer.speed(0)

drawBrickWallOffset()
turtle.done()
