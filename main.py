from turtle import Turtle,Screen
import random,time
from snake import Snake 
from food import Food
from score import Scoreboard
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

new_snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(new_snake.Up,"Up")
screen.onkey(new_snake.down,"Down")
screen.onkey(new_snake.left,"Left")
screen.onkey(new_snake.right,"Right")

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()
    
    # detect when food is collided with snake  
    if new_snake.head.distance(food)<15:
        food.refresh()
        new_snake.extent()
        score.increaseScore()

    # Detect collition with wall
    if new_snake.head.xcor()> 280 or new_snake.head.xcor()<-280 or new_snake.head.ycor()>280 or new_snake.head.ycor()<-280:
        is_game_on=False
        score.gameOver()

    # Detect collision with tail
    # if the heads collides with any segment in the tail
    # Trigger Game Over
    for segment in new_snake.segments:
        if segment==new_snake.head:
            pass
        elif new_snake.head.distance(segment)<10:
            is_game_on=False
            score.tail_msg()
            score.gameOver()
        
screen.exitonclick()
