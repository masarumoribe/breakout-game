from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.color("white")
        self.shape("circle")
        self.penup()
        self.sety(-270)
        self.x_move = 3
        self.y_move = 3

    def create_ball(self):
        pass

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def destroy(self):
        self.clear()
