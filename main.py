import math
import random
import turtle

# This is a turtle race game inspired by the Raspberry Pi Foundation
win_length = 500
win_height = 500
turtles = 7
turtle.screensize(win_length, win_height)


class Racer(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.score = 0
        self.player = turtle.Turtle()
        self.player.shape('turtle')
        self.player.color(color)
        self.player.penup()
        self.player.setpos(pos)
        self.player.setheading(90)

    def move(self):
        r = random.randrange(1, 20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.player.pendown()
        self.player.forward(r)

    def reset(self):
        self.player.penup()
        self.player.setpos(self.pos)


def start_game():
    racer_list = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", 'yellow', 'magenta', 'orange', 'purple']
    start_pos = -(win_length/2) + 20
    for t in range(turtles):
        new_pos_x = start_pos + t * win_length//turtles
        racer_list.append(Racer(colors[t],(new_pos_x, -230)))
        racer_list[t].player.showturtle()

    run = True
    while run:
        for r in racer_list:
            r.move()
        max_distance = 0
        winners = []
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

    # oldScore = []
    # file = open('scores.txt', 'r')
    # for line in file:
    #     l = line.split()
    #     color = l[0]
    #     score = l[1]
    #     oldScore.append([color, score])
    #
    # file.close()
    #
    # file = open('scores.txt', 'w')
    #
    # for entry in oldScore:
    #     for winner in max_color:
    #         if entry[0] == winner:
    #             entry[1] = int(entry[1]) + 1
    #
    #     file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')
    #
    #
    # file.close()


def setup_file(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + ' 0 \n')
    file.close()


setup_file("scores.txt", ["red", "green", "blue", 'yellow', "magenta", "orange", "purple"])


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
