"""Creates a paddle according to the specified co-ordinates"""
from turtle import Turtle, position


class Paddle(Turtle):
    pos = 0
    paddle_speed=20
    def __init__(self, position):
        self.pos = position
        super().__init__()  # Creates an object of Super class Turtle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1,outline=2)

        self.penup()
        self.goto(x=position, y=0)
        """
        Older method
        self.penup()
        self.hideturtle()
        self.speed(10)
        self.goto(x=position, y=0)
        self.showturtle()
        self.speed(5)"""

    # Moving the paddle up
    # TODO: Bug, Pressing the up/down continuosly speeeds up the turtle, calibrate to take only one key press at a time
    def go_up(self):
        if (self.ycor() < 240):
            new_y = self.ycor() + self.paddle_speed
            self.goto(self.xcor(), new_y)
        """while (self.ycor() < 245):
            new_y = self.ycor() + 5  # TODO: Try adding continous movement instead of only 20 steps
            self.goto(self.xcor(), new_y)
        if (self.ycor() == 245):
            self.go_down()"""

    # Moving the paddle down
    def go_down(self):
        if (self.ycor() > -240):
            new_y = self.ycor() - self.paddle_speed
            self.goto(self.xcor(), new_y)
        """while (self.ycor() > -245):
            new_y = self.ycor() - 5
            self.goto(self.xcor(), new_y)
        if (self.ycor() == -245):
            self.go_up()"""

    def reset_paddle(self):
        self.paddle_speed = 20
        self.goto(self.pos, 0)
