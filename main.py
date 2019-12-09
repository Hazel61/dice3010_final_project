import math
import random
import turtle
import os.path

# This is a turtle race game inspired by the Raspberry Pi Foundation. Set the screen size and the number of turtles to
# race.
win_length = 500
win_height = 500
turtles = 7
turtle.screensize(win_length, win_height)

# The Racer class represents an individual racer within this turtle racing game.  Takes one parameter: the default
# object. Each racer has properties that show its color, shape, position, direction, and score.


class Racer(object):
    # function to instantiate an individual racer. Takes three parameters: self, a color, and a position.
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.score = 0
        self.racer = turtle.Turtle()
        self.racer.shape('turtle')
        self.racer.color(color)
        self.racer.penup()
        self.racer.setpos(pos)
        self.racer.setheading(90)

    # Assign a random move for a turtle. Takes one parameter: the racer object.
    def move(self):
        r = random.randrange(1, 20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.racer.pendown()
        self.racer.forward(r)


# Function to draw start and finish lines.
def draw_lines():
    # Draw the start line
    start_line = (-300, -(win_length / 2) + 10)
    finish_line = (-300, 230)
    line_pen = turtle.Turtle()
    line_pen.pensize(5)
    line_pen.color('yellow')
    line_pen.penup()
    line_pen.goto(start_line)
    line_pen.setheading(0)
    line_pen.pendown()
    line_pen.forward(600)
    line_pen.penup()

    # Draw the finish line
    line_pen.pensize(5)
    line_pen.color('red')
    line_pen.penup()
    line_pen.goto(finish_line)
    line_pen.setheading(0)
    line_pen.pendown()
    line_pen.forward(600)
    line_pen.penup()


# Function to initiate the text file to hold the seven turtle colors and a initial score of zero for each. Takes two
# parameters: the name of the text file to hold scores, and a list of colors for turtles.
def setup_file(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + ' 0 \n')
    file.close()


# Function to update each racers score in a text file. Takes one parameter: a list of racers to update.
def update_scores(racers):
    with open('scores.txt', 'w') as f:
        for racer in racers:
            f.write(str(racer.color) + ' ' + str(racer.score) + '\n')


# Main function that runs game.
def start_game():
    racer_list = []
    turtle.clearscreen()
    turtle.hideturtle()
    start_pos = -(win_length / 2) + 20
    colors = ["red", "green", "blue", 'yellow', 'magenta', 'orange', 'purple']
    draw_lines()
    # Iterate through each of the 7 turtles and position then at the start line.
    for t in range(turtles):
        new_pos_x = start_pos + t * win_length // turtles
        racer_list.append(Racer(colors[t], (new_pos_x, -230)))
        racer_list[t].racer.showturtle()
    # check to see if the file to hold scores exists. Make and/or update file.
    if not os.path.exists('scores.txt'):
        setup_file("scores.txt", colors)
    else:
        # read the file for scores
        file = open('scores.txt', 'r')
        for line in file:
            color, score = line.split()
            racer = next(racer for racer in racer_list if racer.color == color)
            racer.score = int(score)
        file.close()
    # more racers to finish line.
    run = True
    while run:
        for r in racer_list:
            r.move()
        max_distance = 0
        winners = []
        # Declare winner.
        for r in racer_list:
            if r.pos[1] > 230 and r.pos[1] > max_distance:
                max_distance = r.pos[1]
                winners = [r]
                r.score += 1
            elif r.pos[1] > 230 and r.pos[1] == max_distance:
                max_distance = r.pos[1]
                winners.append(r)
                r.score += 1

        if len(winners) > 0:
            run = False
            print('The winner is: ' + ', '.join([winner.color for winner in winners]))

    update_scores(racer_list)


start = input('Would you like to play? ')
if start.upper() == "YES":
    start_game()

while True:
    print('-----------------------------------')
    start = input('Would you like to play again? ')
    if start.upper() == "YES":
        start_game()
    else:
        break
