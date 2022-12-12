from turtle import Turtle

import time


class Ball(Turtle):
    move_xcor = 10
    move_ycor = 10
    timer = 0.1

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(x=0, y=0)
        self.speed(0.5)

    def move(self):
        new_x = self.xcor() + self.move_xcor
        new_y = self.ycor() + self.move_ycor
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_ycor *= -1

    def paddle_bounce(self):
        self.move_xcor *= -1
        self.speed(self.speed())
        self.timer /= 1.15

    def reset_ball(self):
        time.sleep(1)
        self.goto(0, 0)
        self.move_xcor *= -1
        self.move_ycor *= -1
        self.timer = 0.1
