import random
import turtle
t = turtle.Turtle()

def pen(color):
    t.color(color)

def move():
    t.ht()
    t.pu()
    x = random.randint(-4,4)
    y = random.randint(-4,4)
    t.goto(x,y)
    t.pd()

def firework(size):
    for x in range(20):
         t.fd(size)
         t.rt(180-(360/20))

def fire():
  global stop
  stop = 0
  t.speed(0)
  pen('red')
  for i in range(2):
      color_r = hex(random.randint(0x10, 0xfa))[2:]
      color_g = hex(random.randint(0x10, 0xfa))[2:]
      color_b = hex(random.randint(0x10, 0xfa))[2:]
      pen('#'+color_r+color_g+color_b)
      firework(random.randrange(1, 3))
      move()
  t.clear()