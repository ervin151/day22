from turtle import Turtle
from my_turtle import MyTim
import random

def random_color256()-> tuple:
    r = random.randint(0,200)
    g = random.randint(0,200)
    b = random.randint(0,200)
    
    # r = random.randint(0,50)
    # g = random.randint(0,50)
    # b = random.randint(0,50)

        
    # r = random.randint(200,250)
    # g = random.randint(200,250)
    # b = random.randint(200,250)
    
    return(r,g,b)
    

class Car(Turtle):
    def __init__(self,pos_num: int = 1,stretch: int = 2,shape:str = 'circle'):
        super().__init__(shape=shape)

        rand_x = random.randint(-400,400)
        self.penup()
        self.goto(rand_x,pos_num * 30 - 250)
        
        self.setheading(180)
        self.shapesize(stretch_len=stretch,stretch_wid=1)
        
        self.color(random_color256())
        self.length = 10 * stretch
        self.rand_speed = random.randint(3,10)


        pass
    def move(self,level : int = 1)->None:
        step = level * 0.1 * self.rand_speed
        self.forward(step)
        
        if self.xcor() < -400 :
            self.goto(400,self.ycor())
            stretch = random.randint(2,5)
            
            self.color(random_color256())
            self.length = 10 * stretch
            self.rand_speed = random.randint(3,10)
            

        pass

    def collision_with_turtle(self,tim : MyTim ) -> bool:
        tim_y = tim.ycor()
        tim_x = tim.xcor()
        car_y = self.ycor()
        car_x = self.xcor()
        car_lenght = self.length

        if abs (car_y - tim_y) < 20 :
            if abs(car_x - tim_x) < car_lenght:
                return True
        return False
    
        pass    


class Trafic:
    def __init__(self):
        self.cars = []
        for i in range(3,20) :
            car_len = random.randint(2,4)
            car = Car(pos_num=i,shape='square',stretch=car_len)
            self.cars.append(car)
    
    def move(self,level)-> None:
        for car in self.cars:
            car.move(level)
            
    def collision(self,tim : MyTim)->False:
        
        for car in self.cars :
            if car.collision_with_turtle(tim) :
                return True
        return False
        pass

        