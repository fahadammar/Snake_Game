from turtle import Turtle, Screen
from snake import Snake
import time

game_on_flag = True

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("___SNAKE___GAME___")
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_on_flag:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
