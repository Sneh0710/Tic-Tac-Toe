import turtle as tr
t = tr.Turtle()

def set_screen():
    # Setup screen and background
    tr.bgcolor("black")
    tr.ht()
    sc = tr.Screen()
    sc.bgpic(picname= "s:\TrainingHub\Python\Scripts\TicTacToe\\bg.gif")
    sc.title("Misty's Tic Tac Toe")
    sc.setup(800,800)
    sc.setworldcoordinates(-5,-5,5,5)
    return sc

def set_turtle(color):
    t.ht()
    t.speed(0)
    t.color(color)

def set_string(str, x, y, color, style):
    set_turtle(color)
    t.up()
    t.goto(x,y)
    t.down()
    t.write(str, font=style, align="center")    
    t.up()

def drw_board():
    set_turtle("grey")
    t.seth(0)
    t.up()
    t.goto(-3,1)
    t.down()
    t.fd(6)
    t.up()
    t.goto(-3,-1)
    t.down()
    t.fd(6)
    t.seth(270)
    t.up()
    t.goto(-1,3)
    t.down()
    t.fd(6)
    t.up()
    t.goto(1,3)
    t.down()
    t.fd(6)    
    t.up()

def drw_result(err):
    set_turtle("green yellow") 
    t.pensize(3)
    t.speed(4)
    t.up()
    if err == 1:
        t.seth(270)
        t.goto(-2,3)
        t.down()
        t.fd(6)
    elif err == 2:
        t.seth(270)
        t.goto(0,3)
        t.down()
        t.fd(6)
    elif err == 3:
        t.seth(270)
        t.goto(2,3)
        t.down()
        t.fd(6)
    elif err == 4:
        t.seth(0)
        t.goto(-3,2)
        t.down()
        t.fd(6)
    elif err == 5:
        t.seth(0)
        t.goto(-3,0)
        t.down()
        t.fd(6)
    elif err == 6:
        t.seth(0)
        t.goto(-3,-2)
        t.down()
        t.fd(6)
    elif err == 7:
        t.seth(-45)
        t.goto(-3,3)
        t.down()
        t.fd(8.48)
    elif err == 8:
        t.seth(45)
        t.goto(-3,-3)
        t.down()
        t.fd(8.48)
    t.pensize(5)    
    t.up()

def drw_circle(x,y):
    set_turtle("pale green")
    t.pensize(5)
    t.up()
    t.goto(x,y-0.7)
    t.down()
    t.seth(0)
    t.circle(0.7, steps=50)    
    t.up()

def drw_x(x,y):
    set_turtle("light coral")
    t.pensize(5)
    t.up()
    t.goto(x-0.6,y-0.6)
    t.down()
    t.goto(x+0.6,y+0.6)
    t.up()
    t.goto(x-0.6,y+0.6)
    t.down()
    t.goto(x+0.6,y-0.6)    
    t.up()

def curve():
    t.speed(0)
    for i in range(5):
        t.right(35)
        t.forward(0.21)

def drw_heart(x,y):
    set_turtle("hot pink")
    t.pensize(5)
    t.up()
    t.goto(x,y-0.7)
    t.down()
    t.seth(130)
    t.forward(1)
    
    # Draw the left curve
    curve()
    t.seth(80)
  
    # Draw the right curve
    curve()
    
    t.seth(230)
    # Draw the right line
    t.forward(1)    
    t.up()


def drw_triangle(x,y):
    set_turtle("yellow")
    t.pensize(5)
    t.up()
    t.goto(x-0.7,y-0.6)
    t.down()
    t.seth(60)
    t.fd(1.4)
    t.seth(-60)
    t.fd(1.4)
    t.seth(180)
    t.fd(1.4)
    t.up()

def drw_square(x,y):
    set_turtle("sky blue")
    t.pensize(5)
    t.up()
    t.goto(x-0.7,y-0.7)
    t.down()
    t.seth(90)
    t.fd(1.4)
    t.seth(0)
    t.fd(1.4)
    t.seth(-90)
    t.fd(1.4)
    t.seth(180)
    t.fd(1.4)
    t.up()

def drw_star(x,y):
    set_turtle("royal blue")
    t.pensize(5)
    t.up()
    t.goto(x-0.7,y+0.15)
    t.down()
    t.seth(0)
    for i in range(5):
 
        # moving turtle 100 units forward
        t.forward(1.4)
 
        # rotating turtle 144 degree right
        t.right(144)
    t.seth(0)    
    t.up()

def drw_symbol(num, x, y):
    if num == 1:
        drw_circle(x, y)
    elif num == 2:
        drw_triangle(x, y)
    elif num == 3:
        drw_square(x, y)
    elif num == 4:
        drw_x(x, y)
    elif num == 5:
        drw_heart(x, y)
    else:
        drw_star(x, y)
    
    