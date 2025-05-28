# Let's Make Turtle Racing Game
from turtle import Turtle,Screen
import random
timmy = Turtle(shape="turtle")
jimmy = Turtle(shape="turtle")
shelby = Turtle(shape="turtle")
rowan = Turtle(shape="turtle")
andrew = Turtle(shape="turtle")
norman = Turtle(shape="turtle")
reznov = Turtle(shape="turtle")
viladmir = Turtle(shape="turtle")
pushkin = Turtle(shape="turtle")
trump = Turtle(shape="turtle")

colors = ["dark blue","dark green","red","yellow","gold","black","peru","pink","firebrick","orange"]
all_turtles = [timmy,jimmy,shelby,rowan,andrew,norman,reznov,viladmir,pushkin,trump]

# Let's Make Turtles
def timmy_direction():
    timmy.color(colors[0])
    timmy.penup()
    timmy.goto(x=-330,y=-200)

def jimmy_direction():
    jimmy.color(colors[1])
    jimmy.penup()
    jimmy.goto(x=-330,y=-150)

def shelby_direction():
    shelby.color(colors[2])
    shelby.penup()
    shelby.goto(x=-330,y=-100)

def rowan_direction():
    rowan.color(colors[3])
    rowan.penup()
    rowan.goto(x=-330,y=-50)

def andrew_direction():
    andrew.color(colors[4])
    andrew.penup()
    andrew.goto(x=-330, y=0)

def norman_direction():
    norman.color(colors[5])
    norman.penup()
    norman.goto(x=-330, y=50)

def reznov_direction():
    reznov.color(colors[6])
    reznov.penup()
    reznov.goto(x=-330, y=100)

def viladmir_direction():
    viladmir.color(colors[7])
    viladmir.penup()
    viladmir.goto(x=-330, y=150)

def pushkin_direction():
    pushkin.color(colors[8])
    pushkin.penup()
    pushkin.goto(x=-330, y=200)

def trump_direction():
    trump.color(colors[9])
    trump.penup()
    trump.goto(x=-330, y=250)

timmy_direction()
jimmy_direction()
shelby_direction()
rowan_direction()
andrew_direction()
norman_direction()
reznov_direction()
viladmir_direction()
pushkin_direction()
trump_direction()

screen = Screen()
user_input = screen.textinput("Guess the Color","Which Turtle Will Win?")

is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        random_number = random.randint(0,9)
        turtle.forward(random_number)

        if turtle.xcor() >=330:
            wining_color = turtle.pencolor()
            is_game_on = False
            if user_input == wining_color:
                print(f"Congratulation {wining_color} Turtle Has Won.")
            else:
                print(f"Oh No {wining_color} has Lost The Game.")













screen.exitonclick()
