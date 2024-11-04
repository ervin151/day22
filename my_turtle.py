from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class MyTim(Turtle):
    def __init__(self, shape = "turtle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        
        self.penup()
        self.color("green")

        self.goto(x=0,y=-230)
        self.setheading(LEFT)


    def step_up(self,step:int = 5)-> None:
        self.setheading(UP)
        self.forward(step)
    def step_down(self,step:int = 5)-> None:
        self.setheading(DOWN)
        self.forward(step)
    def step_left(self,step:int = 5)-> None:
        self.setheading(LEFT)
        self.forward(step)
    def step_right(self,step:int = 5)-> None:
        self.setheading(RIGHT)
        self.forward(step)



    
