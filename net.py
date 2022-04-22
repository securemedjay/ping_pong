from turtle import Turtle


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(0, -300)
        self.speed("fastest")
        self.color("white")
        self.pensize(5)
        self.penup()
        self.setheading(90)
        self.hideturtle()

    def draw_net(self):
        self.pendown()
        self.forward(600)
