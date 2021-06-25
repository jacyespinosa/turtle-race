from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
y_position = [-120, -70, -20, 20, 70, 120]
colors = ['red', 'pink', 'yellow', 'green', 'blue', 'purple']
list_of_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (ROYGBV): ").title()

def random_movement():
    return random.randint(0, 20)

for i in range(0, 6):
    turtle_name = Turtle()
    turtle_name.shape('turtle')
    turtle_name.color(colors[i])
    turtle_name.penup()
    turtle_name.goto(x=-230, y=y_position[i])
    list_of_turtles.append(turtle_name)

if user_bet:
    race = True

while race:
    for turtle in list_of_turtles:
        who_won = turtle.pencolor().title()
        if turtle.xcor() > 215 and who_won == user_bet:
            print(f"{who_won} won the race. You guessed it right!")
            race = False
        elif turtle.xcor() > 215 and who_won != user_bet:
            print(f"{who_won} won the race. You guessed WRONG!")
            race = False
        else:
            distance = random_movement()
            turtle.forward(distance)

screen.exitonclick()