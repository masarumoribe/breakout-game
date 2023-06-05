from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick

TOTAL_BRICKS = 64
BRICKS = []
x = -355
y = 280

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

print(BRICKS)

paddle = Paddle()
ball = Ball()
for row in range(8):
    row = []
    for j in range(8):
        j = Brick(x, y, BRICKS)
        x += 100
        row.append(j)
    BRICKS.append(row)
    y -= 30
    x = -355

print(len(BRICKS[0]))

screen.listen()
screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()
    if (
        ball.ycor() < paddle.ycor() + 20
        and paddle.xcor() - 80 < ball.xcor() < paddle.xcor() + 80
    ):
        ball.bounce_y()

    for row in BRICKS:
        for brick in row:
            if (
                brick.xcor() - 45 < ball.xcor() < brick.xcor() + 45
                and brick.ycor() - 20 < ball.ycor() < brick.ycor() + 20
            ):
                if abs(ball.ycor() - brick.ycor()) > abs(ball.xcor() - brick.xcor()):
                    ball.bounce_x()
                    brick.destroy()
                    row.remove(brick)
                else:
                    ball.bounce_y()
                    brick.destroy()
                    row.remove(brick)


screen.exitonclick()
