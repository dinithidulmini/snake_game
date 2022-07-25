from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.m_up,key="Up")
screen.onkey(fun=snake.m_down,key="Down")
screen.onkey(fun=snake.m_right,key="Right")
screen.onkey(fun=snake.m_left,key="Left")

game_is_on = True

while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -298 or snake.turtles[0].ycor() > 298 or snake.turtles[0].ycor() < -298:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.turtles:
        if snake.turtles[0] != segment:
            if snake.turtles[0].distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
