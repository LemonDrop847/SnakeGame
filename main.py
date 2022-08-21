from ast import Pass
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scorebrd
from walls import Walls
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scorebrd()
walls=Walls()

walls.Drawwall()
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()
        
    #wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        scoreboard.gameover()

    #tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on=False
            scoreboard.gameover()

screen.exitonclick()