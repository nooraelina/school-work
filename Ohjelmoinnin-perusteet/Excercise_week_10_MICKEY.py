# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:47:11 2019

@author: noora
"""
import turtle
def draw_circle(color, radius, x, y):   # Ympyrän funktio
    t.penup()
    t.fillcolor(color)      # Väri
    t.goto(x,y)             # Kohta mistä aloitetaan piirtämään
    t.pendown()
    t.begin_fill()
    t.circle(radius)        # Ympyrä
    t.end_fill()
    
def oval(color, color2, length, width, outline, x, y, tilt):   # Ovaalin funktio
    t.penup()
    t.fillcolor(color)      # Väri
    t.pencolor(color2)      # Rajojen väri
    t.goto(x,y)             # Kohta mihin kuvio tulee
    t.settiltangle(tilt)    # Ovaalin kaltevuus
    t.shape("circle")       # Ovaalin muodon määritys
    t.shapesize(length,width,outline)   # Ovaalin koon määritys
    t.stamp()               # leimaa muoto kuvaan
        
def line(color, size, rad, x, y, degr, heading):
    t.penup()
    t.pencolor(color)   # Kynän väri
    t.pensize(size)     # Koko
    t.goto(x,y)         # Aloituskohta
    t.setheading(heading)   # mihin suuntaan asteina
    t.pendown()
    t.circle(rad, degr)     # ympyrän koko, paljonko piirretään(asteina)
        
if __name__ == '__main__':
    turtle.speed(6)             # kynän nopeus
    win = turtle.Screen()       # uusi ikkuna
    win.bgcolor("#ffb1b6")      # taustaväri
    win.title("Mickey")         # Ikkunan nimi
    t = turtle.Turtle()
    t.hideturtle()              # Piilotetaan turtlen osoitin
    # toiminnot alkaa tästä
    # Mustat osat
    draw_circle("black", 100, 0, 0)     # pää
    draw_circle("black", 60, 100, 150)    # oik korva
    draw_circle("black", 60, -100, 150)   # vas korva
    # ihonväriset osat
    oval("#ddbc9d", "#ddbc9d", 7, 5, 1, 20, 120, 0)
    oval("#ddbc9d", "#ddbc9d", 7, 5, 1, -20, 120, 0)
    oval("black", "black", 5, 3, 1, -45, 33, 60)
    oval("black", "black", 5, 3, 1, 45, 33, -60)
    oval("black", "black", 7, 5, 1, 0, 48, 0)
    oval("#ddbc9d", "#ddbc9d", 5, 3, 1, -45, 35, 60)
    oval("#ddbc9d", "#ddbc9d", 5, 3, 1, 45, 35, -60)
    oval("#ddbc9d", "#ddbc9d", 7, 5, 1, 0, 50, 0)
    # Suu
    oval("black", "black", 7, 4, 1, 0, 55, 0)
    oval("#ddbc9d", "#ddbc9d", 5, 6, 1, 0, 55, 0)
    oval("#ddbc9d", "#ddbc9d", 5, 4, 1, 0, 80, 0)
    # Silmät
    oval("white", "black", 3.5, 1.5, 1, -18, 110, 0) # vas silmänpohja
    oval("white", "black", 3.5, 1.5, 1, 18, 110, 0) # oik silmänpohja
    oval("black", "black", 1.2, 0.7, 1, -15, 88, 0) # vas iris
    oval("black", "black", 1.2, 0.7, 1, 15, 88, 0) # oik iris
    # Nenä
    oval("black", "black", 1.5, 2.5, 1, 0, 57, 0)
    # Viivat
    line("black", 1, 60, 26, 73, 55, -205) # suun viiva
    line("black", 2, 65, -60, 45, 140, -70) # suun viiva
    line("black", 1, 20, -50, 45, 55, -200) # vas hymykuoppa
    line("black", 1, 20, 70, 42, 55, -220) # oik hymykuoppa
    win.exitonclick()