from turtle import Turtle

WALLAT = 290
class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()

    def Drawwall(self):
        self.goto(WALLAT,-WALLAT)
        self.pendown()
        self.goto(WALLAT,WALLAT)
        self.goto(-WALLAT,WALLAT)
        self.goto(-WALLAT,-WALLAT)
        self.goto(WALLAT,-WALLAT)
        self.hideturtle()
