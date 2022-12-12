
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen_size_height = 600
screen_size_width = 800

screen = Screen()
screen.bgpic("background.gif")
screen.setup(height=screen_size_height, width=screen_size_width)
screen.title("Pong Game")
screen.tracer(0)  # Tracer put to zero, no animation

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True


# screen.tracer(1)

def turn_off():
    global game_is_on
    game_is_on = False


while game_is_on:
    screen.update()
    time.sleep(ball.timer)
    ball.move()
    screen.update()
    # Detect Collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        right_paddle.paddle_speed +=5
        left_paddle.paddle_speed +=5

    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce()
    if ball.xcor() > 380:

        ball.reset_ball()
        right_paddle.reset_paddle()
        left_paddle.reset_paddle()
        score.add_left()
        # Reset ball
    if ball.xcor() < -380:

        ball.reset_ball()
        right_paddle.reset_paddle()
        left_paddle.reset_paddle()
        score.add_right()
        # Reset ball


screen.exitonclick()
