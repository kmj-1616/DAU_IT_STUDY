#from turtle import *
import turtle as t
def draw_circle(n):
    m = 360/n
    for i in range(n):
        t.circle(100)
        t.left(m)
def draw_square(size):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size+=5
def draw_line():
    t.forward(100)
    t.backward(100)

#t.color('red')
#for i in range(20):
#    draw_line()
#    t.left(18)

#draw_circle(12)
#for i in range(10,200,20):
#    draw_square(i)
#draw_square(10)
#t.done()