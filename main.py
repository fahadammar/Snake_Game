from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("___SNAKE___GAME___")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

scoreboard.welcome_screen(screen=screen)


def startGame():
    game_on_flag = True
    while game_on_flag:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # DETECT COLLISION WITH THE FOOD
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # DETECT COLLISION WITH WALL
        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            game_on_flag = False
            scoreboard.game_over()

        for snake_seg in snake.turtle_instance_list[1:]:
            if snake.head.distance(snake_seg) < 10:
                game_on_flag = False
                scoreboard.game_over()


screen.ontimer(startGame, 8000)

screen.exitonclick()
