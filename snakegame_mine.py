from turtle import Turtle,Screen
import turtle
import time


screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Snake Game")

tur=Turtle("square")
tur.color("white")
tur.shapesize(1,3,1)
time.sleep(0.1)

game_on=True
while game_on:
    tur.penup() 
    tur.forward(60)
    tur.left(90)


screen.exitonclick()