import turtle

def onR(): ## Reset the board
    global turn
    global board
    
    pointer.clear()
    turn = 0
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    
    draw_board()
    
def onS(): ## Save the board
    global turn
    global board
    global turn_saved
    global board_saved
    
   # Save the turn and board
    turn_saved = turn
    for i in range(3):
        for j in range (3):
            board_saved[i][j] = board[i][j]
            
    print(turn_saved)
    print(board_saved)
    
def onO() : ## Open the saved board
    global turn
    global board
    global turn_saved
    global board_saved
    
    pointer.clearstamps() 
    print(turn_saved)
    print(board_saved)
    
    draw_board()

    ## Go to the saved setup
    turn = turn_saved
    board = board_saved    
   
    for i in range(3):
        for j in range (3):
            if board[i][j] != 0:
                pointer.goto(0.5 + j, 0.5 + i)
                if board[i][j] == 1:
                    pointer.shape("circle")
                    pointer.stamp()
                else:
                    pointer.shape("square")
                    pointer.stamp()
                    
            
def clickFunc(x,y):
    global turn
    global board
    
    ## First Row
    if 0.1<x<0.9 and 0.1<y<0.9: #0
        pointer.goto(0.5,0.5)
        if board[0][0] == 0: #the spot is empty
            if turn%2 == 0:
                pointer.shape("circle")
                board[0][0] = 1
            else:
                pointer.shape("square")
                board[0][0] = 2
    elif 1.1<x<1.9 and 0.1<y<0.9: #1
        pointer.goto(1.5,0.5)
        if board[0][1] == 0: #the spot is empty
            if turn %2 == 0:
                pointer.shape("circle")
                board[0][1] = 1
            else:
                pointer.shape("square")
                board[0][1] = 2            
    elif 2.1<x<2.9 and 0.1<y<0.9: #2
        pointer.goto(2.5,0.5)
        if board[0][2] == 0: #the spot is empty
            if turn %2 == 0:
                pointer.shape("circle")
                board[0][2] = 1
            else:
                pointer.shape("square")
                board[0][2] = 2     
    
    ## Second Row
    elif 0.1<x<0.9 and 1.1<y<1.9: #3
        pointer.goto(0.5,1.5)
        if board[1][0] == 0: #the spot is empty
            if turn%2 == 0:
                pointer.shape("circle")
                board[1][0] = 1
            else:
                pointer.shape("square")
                board[1][0] = 2
    elif 1.1<x<1.9 and 1.1<y<1.9: #4
        pointer.goto(1.5,1.5)
        if board[1][1] == 0: #the spot is empty
            if turn %2 == 0:
                pointer.shape("circle")
                board[1][1] = 1
            else:
                pointer.shape("square")
                board[1][1] = 2
    elif 2.1<x<2.9 and 1.1<y<1.9: #5
        pointer.goto(2.5,1.5)
        if board[1][2] == 0: #the spot is empty
            if turn %2 == 0:
                pointer.shape("circle")
                board[1][2] = 1
            else:
                pointer.shape("square")
                board[1][2] = 2
                
    ## Third Row
    elif 0.1<x<0.9 and 2.1<y<2.9: #6
        pointer.goto(0.5,2.5)
        if board[2][0] == 0: #the spot is empty
            if turn %2 == 0:
                pointer.shape("circle")
                board[2][0] = 1
            else:
                pointer.shape("square")
                board[2][0] = 2
    elif 1.1<x<1.9 and 2.1<y<2.9: #7
        pointer.goto(1.5,2.5)
        if board[2][1] == 0: #the spot is empty
            if turn %2 == 0:
                pointer.shape("circle")
                board[2][1] = 1
            else:
                pointer.shape("square")
                board[2][1] = 2
    elif 2.1<x<2.9 and 2.1<y<2.9: #8
        pointer.goto(2.5,2.5)
        if board[2][2] == 0: #the spot is empty
            if turn %2 == 0:
                pointer.shape("circle")
                board[2][2] = 1
            else:
                pointer.shape("square")
                board[2][2] = 2
   
    pointer.stamp()
    print(board)
    
    turn += 1
    
    player = check_winner()
    pointer.goto(1.5,1.5)
    if player == 1 :
        pointer.write("Player 1 Won", align="center", font=("Arial", 24, "normal"))
    elif player == 2 :
        pointer.write("Player 2 Won", align="center", font=("Arial", 24, "normal"))
    elif turn == 9 :
        pointer.write("Draw", align="center", font=("Arial", 24, "normal"))
    
    return
    
def check_winner():
    global board
    
    ## Check for diagonal wins
    if 0 != board[0][0] == board[1][1] == board[2][2] or 0 != board[2][0] == board[1][1] == board[0][2]: 
            return board[1][1]
            
    ## Check for row and column wins    
    for i in range(3):   
        if 0 != board[i][0] == board[i][1] == board[i][2]: ## Row Wins
            return board[i][0]
        elif 0 != board[0][i] == board[1][i] == board[2][i]: ## Column Wins
            return board[0][i]
            
    # There is no winner
    return 0   
        
def draw_board():
    pointer.width(3) 
    draw_line(0,1,3,1) # First horizontal line
    draw_line(0,2,3,2) # Second horizontal line
    draw_line(1,0,1,3) # First vertical line
    draw_line(2,0,2,3) # Second horizontal line
   
def draw_line(x1,y1,x2,y2):
    pointer.goto(x1,y1)
    pointer.pendown()
    pointer.goto(x2,y2)
    pointer.penup()

## Main function
screen = turtle.Screen()
screen.screensize(700,700) #sets the size of screen in pixels 
screen.setworldcoordinates(0,0,3,3) #sets up coordinate system
screen.onclick(clickFunc) #tells turtle to run clickFunc when the user clicks
                          #the click func receives the x and y coords of the click

screen.onkey(onR,"r")
screen.onkey(onS,"s")
screen.onkey(onO,"o")

pointer = turtle.Turtle()
pointer.up()
pointer.shape("circle")
pointer.color("black")
pointer.speed(0)
pointer.hideturtle()

draw_board()

turn = 0
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
         
turn_saved = 0
board_saved = [[0,0,0],
               [0,0,0],
               [0,0,0]]

screen.listen() 

turtle.done()

turtle.exitonclick() # Prevent the turtle window from disappearing