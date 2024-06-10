from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.title('PONG')
screen.setup(width=800, height=600)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
