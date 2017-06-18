# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
renderCF.py

Author: Christopher Ayling

Module for rendering a game of connect four

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import turtle

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def setup_board(width, height, square_size, bg_color = 'light blue'):
    '''
    Sets up the board.
    '''
    turtle.setup(width = width * square_size, height = height * square_size)
    turtle.bgcolor(bg_color)
    
    turtle.speed("fastest")
    turtle.ht()
    turtle.pu()
    turtle.goto(-(width * square_size)/2,-(height * square_size)/2)
    
    
    
def draw_board(board, square_size, height):
    '''
    Draws each column of counters.
    '''
    orig_x, orig_y = turtle.xcor(), turtle.ycor()
    
    for column in board:
        draw_column(column, square_size)
        turtle.goto(turtle.xcor() + square_size, -(height * square_size)/2)
        
    turtle.goto(orig_x, orig_y)

    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
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