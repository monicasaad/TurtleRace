# import required modules
import random
from turtle import Turtle, Screen

# create screen object
my_screen = Screen()
# set height and width of screen
my_screen.setup(width=500, height=400)

# list with turtle colours
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
# list to hold all turtle object
turtles_list = []

# variable to hold starting y-coordinate of turtle object
y_cord = -125

# loop to create multiple turtle objects
for turtle_index in range(0, 6):
    # create turtle object
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colours[turtle_index])
    # set starting position
    new_turtle.goto(x=-230, y=y_cord)
    # add turtle object to turtles_list
    turtles_list.append(new_turtle)
    y_cord += 50

# variable to check if race is on, start by setting to False
is_race_on = False

# get user input for bet
bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color "
                                                        "(red/yellow/green/blue/purple):").lower()

# switch is_race_on after user has made their bet
is_race_on = True

# loop for turtles to move when race is running
while is_race_on:
    # loop through turtles list and move each turtle forwards by a random amount
    for turtle in turtles_list:
        turtle.forward(random.randint(1, 10))
        # check if turtle has reached finish line
        if turtle.xcor() >= 230:
            is_race_on = False
            # get colour of winning turtle
            winning_turtle = turtle.pencolor()
            # check if winning_turtle is same as user's bet
            if winning_turtle == bet:
                print(f"You won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You lost. The {winning_turtle} turtle is the winner.")

# keep screen popup open
my_screen.exitonclick()
