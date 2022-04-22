from turtle import Screen
from net import Net
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True
screen = Screen()
screen.bgcolor("green")
screen.setup(width=800, height=600)
screen.title("My Pin Pong")
screen.tracer(0)  # to turn off animation

scoreboard = Scoreboard()

net = Net()
ball = Ball()

net.draw_net()

l_paddle = Paddle((-370, 0))
l_paddle.color("red")
r_paddle = Paddle((350, 0))
r_paddle.color("blue")

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# paddle.create_paddle()


while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()  # to manually turn on the screen
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect if the right paddle misses the ball
    if ball.xcor() > 400:
        ball.reset_ball()
        ball.change_direction()
        scoreboard.l_score += 1
        scoreboard.display_score()

    # Detect if the left paddle misses the ball
    if ball.xcor() < -400:
        ball.reset_ball()
        ball.change_direction()
        scoreboard.r_score += 1
        scoreboard.display_score()

screen.exitonclick()
