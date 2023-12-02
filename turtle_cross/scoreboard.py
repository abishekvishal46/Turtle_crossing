FONT = ("Courier", 24, "normal")
from turtle import Turtle
import player
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-260,260)

        self.write(arg=f"LEVEL: {self.level}",move=False,align="left",font=FONT)
    def inc(self):
        self.level+=1
        self.clear()
        self.write(arg=f"LEVEL: {self.level}", move=False, align="left", font=FONT)

    def end_game(self):
        self.goto(0,0)
        self.write(f"GAME OVER",False, align="center", font=FONT)



