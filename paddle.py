from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.setposition(position)

    def move_up(self):
        new_y = self.ycor() + 40
        self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.setposition(self.xcor(), new_y)
