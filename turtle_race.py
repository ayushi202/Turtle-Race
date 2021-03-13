from turtle import *
import random
is_game_on=False
blue=Turtle()
green=Turtle()
yellow=Turtle()
orange=Turtle()
red=Turtle()
turtles=[blue,green,yellow,orange,red]
blue.shape("turtle")
green.shape("turtle")
yellow.shape("turtle")
orange.shape("turtle")
red.shape("turtle")

blue.color("blue")
green.color("green")
yellow.color("yellow")
orange.color("orange")
red.color("red")

for t in turtles:
    t.penup()


screen=Screen()
user=screen.textinput(title="Pick Your Bet", prompt="Which Turtle will Win the Race? Enter Color: " )
screen.setup(width=800, height=600)
blue.goto(-380,150)
green.goto(-380,75)
yellow.goto(-380,0)
orange.goto(-380,-75)
red.goto(-380,-150)
if user:
    is_game_on=True
while is_game_on:
    for i in turtles:
        if i.xcor()>=380:
            winning_turtle=i.pencolor()
            if winning_turtle==user:
                print("You Won")
            else:
                print(f"The winner of the Race is {winning_turtle} turtle.You lost the bet")
            is_game_on=False
            exit()
            break

        dist=random.randint(1,10)
        i.forward(dist)
        

screen.exitonclick()

