import random
import turtle
from turtle import *
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POS=[(0,0),(-20,0)]



class CarManager(Turtle):

    def __init__(self):
     super().__init__()
     self.cars_2=[]
     self.create_car()
     self.hideturtle()
     self.current_speed=STARTING_MOVE_DISTANCE



    def create_car(self):
        chance=random.randint(1,6)
        if chance==1:
            car=Turtle(shape="square")


            car.shapesize(stretch_len=2,stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))


            car.goto(300,random.randint(-250,250))
            self.cars_2.append(car)

    def move(self):
        for i in self.cars_2:
            i.backward(self.current_speed)
    def increase_speed(self):


            self.current_speed+=MOVE_INCREMENT







