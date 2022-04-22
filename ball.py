from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.setheading(45)
        # self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        # self.move()

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.setposition(x_cor, y_cor)

    def bounce_y(self):
        # change direction along y-axis
        self.y_move *= -1

    def bounce_x(self):
        # change direction along x-axis
        self.x_move *= -1
        self.ball_speed *= 0.9

    def change_direction(self):
        self.y_move *= -1
        self.x_move *= -1

    def reset_ball(self):
        self.home()
        self.ball_speed = 0.1
