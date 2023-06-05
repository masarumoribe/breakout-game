from turtle import Turtle

class Brick(Turtle):
    def __init__(self, x_pos, y_pos, bricks_list):
        super().__init__()
        self.shape("square")
        self.color("purple")
        self.shapesize(stretch_wid=1, stretch_len=4.5)
        self.penup()
        self.setx(x_pos)
        self.sety(y_pos)
        self.bricks_list = bricks_list

    def destroy(self):
        self.hideturtle()
        del self

