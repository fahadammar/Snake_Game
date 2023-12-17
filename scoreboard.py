from turtle import Turtle
import welcome
import time

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
WELCOME_FONT = ("Courier", 8, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def welcome_screen(self, screen):
        print(welcome.show_welcome())
        self.welcomeText()
        screen.ontimer(self.clearScreen, 1000)
        screen.ontimer(self.toText, 2000)

        screen.ontimer(self.clearScreen, 3000)
        screen.ontimer(self.titleText, 4000)

        screen.ontimer(self.clearScreen, 6000)
        screen.ontimer(self.setScoreBoardToTop, 6000)
        screen.ontimer(self.update_board, 7000)

    def welcomeText(self):
        self.goto(0, 0)
        self.write(welcome.show_welcome(), align=ALIGNMENT, font=WELCOME_FONT)

    def toText(self):
        self.goto(0, 0)
        self.write(welcome.show_to(), align=ALIGNMENT, font=WELCOME_FONT)

    def titleText(self):
        self.goto(0, 0)
        self.write(welcome.show_title(), align=ALIGNMENT, font=WELCOME_FONT)

    def setScoreBoardToTop(self):
        self.goto(0, 270)

    def clearScreen(self):
        self.clear()
