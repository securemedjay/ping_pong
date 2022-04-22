from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.setposition(-100, 250)
        self.write(f"{self.l_score}", font=("Courier", 40, "bold"), align="center")
        self.setposition(100, 250)
        self.write(f"{self.r_score}", font=("Courier", 40, "bold"), align="center")
