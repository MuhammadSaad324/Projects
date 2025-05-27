# Let's Build Etch A Sketch Game
from turtle import Turtle,Screen

jimmy = Turtle()
jimmy.shape("turtle")

def forward():
    jimmy.forward(50)

def backward():
    jimmy.backward(50)

def left():
    jimmy.left(20)

def right():
    jimmy.right(20)

def clear():
    jimmy.home()
    jimmy.clear()







screen = Screen()
screen.listen()
screen.onkey(forward,"w")
screen.onkey(backward,"s")
screen.onkey(left,"a")
screen.onkey(right,"d")
screen.onkey(clear,"c")




screen.exitonclick()