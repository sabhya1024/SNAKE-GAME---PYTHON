from turtle import Turtle, Screen
import time
screen = Screen()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt",) as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score = {self.score}, HIGH SCORE : {self.highscore}", align="center", font=('Arial', 11, 'normal'))

    def scoreboard(self):
        self.score += 1
        self.update()

    def gameover(self):
        tim = Turtle()
        tim.goto(0, 100)
        tim.pencolor("white")
        tim.write(arg="Game Over", align="center", font=("Georgia", 45 , "normal") )
        self.update()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.goto(0,270)
        self.update()



