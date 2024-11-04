from turtle import Turtle,Screen
import random

SCREEN_COLOR = 'white'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
CAR_SHAPE = 'square'

class GameScreen(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
       super().__init__(shape, undobuffersize, visible)
       self.scr = Screen()
       self.scr.colormode(255)
       self.scr.bgcolor = SCREEN_COLOR
       self.scr.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
       self.scr.title("Turtle crossing Capstone Game ")
       self.scr.tracer(0)
       self.scr.listen()

       self.level = 1

       pass
 
    def draw_level(self,level:int = 1):
        self.clear()
        self.isvisible = False
        self.penup()
        self.goto(0,200)
      
        self.write(arg=level,align='left',font=('Arial',30,'normal'))
        self.goto(1000,1000)
        pass
    def print_Game_Over(self)-> None:
        self.goto(0,0)
        self.write(arg="Game is Over !!",font=('Arial',30,'normal'),align='center')
        pass

