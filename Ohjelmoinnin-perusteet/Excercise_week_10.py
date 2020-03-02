# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:55:49 2019

@author: noora
"""
import turtle

# Tehtävä 1
def square(n):
    for i in range(4):
        pen.fd(n)
        pen.lt(90)
        
if __name__ == '__main__':
    turtle.speed(1)
    win = turtle.Screen()
    pen = turtle.Turtle()
    square(100)
    win.exitonclick()

# tehtävä 2
def square2(n):
    for i in range(3):
        pen.lt(22.5)
        for i in range(4):
            pen.fd(n)
            pen.lt(90)
    return
        
if __name__ == '__main__':
    turtle.speed(3)
    win = turtle.Screen()
    pen = turtle.Turtle()
    square2(90)
    win.exitonclick()
    
# Tehtävä 3
def hexagon(n):
     pen.lt(30)
     for i in range(6):
         pen.fd(n)
         pen.lt(60)
        
if __name__ == '__main__':
    turtle.speed(3)
    win = turtle.Screen()
    pen = turtle.Turtle()
    hexagon(90)
    win.exitonclick()
    
# Tehtävä 4
def hexagon(n):
     for i in range(5):
         pen.fd(n)
         pen.rt(144)
        
if __name__ == '__main__':
    turtle.speed(3)
    win = turtle.Screen()
    pen = turtle.Turtle()
    hexagon(90)
    win.exitonclick()


