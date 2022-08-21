from turtle import Turtle

ALIGNMENT ="center"
FONT=("Courier",20,"bold")

class Scorebrd(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.updateScore()
        self.hideturtle()
        
    def updateScore(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over - GG ",align=ALIGNMENT,font=FONT)

    def increaseScore(self):
        self.score+=1
        self.clear()
        self.updateScore()

