import time
from turtle import Screen
from player import Player
from car_manager import *
from scoreboard import *
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
sc=Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


def end():
    global game_is_on
    game_is_on = False

game_is_on=True
screen.onkey(end, "w")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()


    for i in car_manager.cars_2:
        if i.distance(player)<20:
            sc.end_game()
            game_is_on=False
    if player.ycor()==280:


        sc.inc()
        player.starting()
        car_manager.increase_speed()










screen.exitonclick()