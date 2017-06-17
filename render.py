import turtle

SQUARE_SIZE = 100
WIDTH = 7
HEIGHT = 6

BG_COLOUR = 'light blue'
P1C = "red"
P2C = "green"

test_column = [P1C, P2C, P1C]
test_board = [[P1C, P2C, P1C],[P1C, P2C, P1C, P1C, P2C, P1C],[P1C, P1C, P1C, P1C, P1C],[],[P2C],[],[P1C, P1C, P1C, P2C]]

def setup_board(width, height, square_size):
    '''
    Sets up the board.
    '''
    turtle.setup(width = width * square_size, height = height * square_size)
    turtle.bgcolor(BG_COLOUR)
    
    turtle.speed("fastest")
    turtle.ht()
    turtle.pu()
    turtle.goto(-(width * square_size)/2,-(height * square_size)/2)
    
    
    
def draw_counter(colour, square_size):
    '''
    Draws a counter of a specific colour.
    '''
    turtle.color("black", colour)
    turtle.begin_fill()
    for corner in range(4):
        turtle.forward(square_size)
        turtle.left(90)
    turtle.end_fill()
    
    
    
def draw_column(column, square_size):
    '''
    Draws a column of counters.
    '''
    turtle.pd()
    for counter in column:
        draw_counter(counter, square_size)
        turtle.goto(turtle.xcor(), turtle.ycor() + square_size)
    turtle.pu()
        
        
    
def draw_columns(board, square_size, height):
    '''
    Draws each column of counters.
    '''
    for column in board:
        draw_column(column, square_size)
        turtle.goto(turtle.xcor() + square_size, -(height * square_size)/2)
        
    

setup_board(WIDTH, HEIGHT, SQUARE_SIZE)
draw_column(test_column, SQUARE_SIZE)
draw_columns(test_board, SQUARE_SIZE, HEIGHT)


turtle.exitonclick()    