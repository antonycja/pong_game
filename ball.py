from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.Y_SPEED = 0.09
        self.X_SPEED = 0.09

    def move(self):
        new_x = self.xcor() + self.X_SPEED
        new_y = self.ycor() + self.Y_SPEED
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.Y_SPEED *= -1

    def bounce_x(self):
        self.X_SPEED *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
