from turtle import Turtle, Screen
from car import Car
from car import Trafic
from screen import GameScreen

from my_turtle import MyTim
import time
import random

# make scree 500 height and any lenght for example 800
"""
car size 20 - size standart for a turtle 
5 is distanse between cars ttqal we have 20 car lines 

20 * 25 = 500

turtle is one turtle 20x20

cars have random color and lenght 3 - 5 turtles 
cars have random speed
cars apear randomly 
"""

game_screen = GameScreen()


# car = Car(shape=CAR_SHAPE,stretch=4)
tim = MyTim()

game_traffic = Trafic()
game_level = 1

game_is_on = True
def turn_game_off(game: bool) -> None:
    global game_is_on
    game_is_on = False
    game = False



game_screen.scr.listen()

game_screen.scr.onkeypress(key='q',fun=turn_game_off)

game_screen.scr.onkeypress(key='Left',fun=tim.step_left)
game_screen.scr.onkeypress(key='Right',fun=tim.step_right)
game_screen.scr.onkeypress(key='Down',fun=tim.step_down)
game_screen.scr.onkeypress(key='Up',fun=tim.step_up)

game_screen.draw_level(2)
game_level = 1
game_screen.draw_level(game_level - 1)
while game_is_on:
    time.sleep(0.01)
    game_screen.scr.update()
    game_traffic.move(game_level)

    if tim.ycor() > 230 :
        game_level += 1
        game_screen.draw_level(game_level - 1)
        tim.goto(0,-230)

    if game_traffic.collision(tim=tim):

        game_screen.print_Game_Over()
        game_is_on = False
        pass
 

    pass
game_screen.scr.exitonclick()