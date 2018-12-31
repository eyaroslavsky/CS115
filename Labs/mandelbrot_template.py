# mandelbrot.py
# Lab 8
#
# Name:

# keep this import line...
from cs5png import *
import turtle

# start your Lab 8 functions here:
def mult( c, n ):
    #TODO

def update(c,n):
    #TODO

def inmset(c,n):
    #TODO

def scale(pix,pixMax,floatMin,floatMax):
    #TODO

def mset():
    width=300
    height=200
    turtle.speed(0)
    turtle.tracer(0,0)
    turtle.screensize(width,height)
    turtle.setworldcoordinates(0,0,width,height)
    turtle.setpos(0,0)
    turtle.penup()
    image=PNGImage(width,height)
    for col in range(width):
        for row in range(height):
            turtle.setpos(col,row)
            #ADD CODE HERE
            if inmset(c,25):
                turtle.dot()
    turtle.update()
    turtle.done()
print(mult(3,4))
print(update(-1,3))
c = 3+4*1j
print(inmset(c,25))
print(scale(100,300,-2,1))

mset()