from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]

    def createsnake(self):
        for position in STARTING_POSITION:
            self.add_seg(position)
        #self.segments[0].color("green")

    def move(self):
        for seg_num in range(len(self.segments)-1 ,0 ,-1):
            newx=self.segments[seg_num-1].xcor()
            newy=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(newx,newy)
        self.head.forward(MOVE_DIST)
    
    def extend(self):
        self.add_seg(self.segments[-1].position())

    def add_seg(self,position):
        new_segment=Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)