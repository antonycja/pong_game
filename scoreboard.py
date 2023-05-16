from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_scoreboard(self):
        self.color("yellow")
        self.goto(-300, 200)
        self.write(self.l_score, align="left", font=("courier", 50, "bold"))

    def r_scoreboard(self):
        self.color("red")
        self.goto(300, 200)
        self.write(self.r_score, align="right", font=("courier", 50, "bold"))

    def title(self):
        self.color("blue")
        self.goto(-75, 220)
        self.write("Score", font=("courier", 40, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.l_scoreboard()
        self.r_scoreboard()
        self.title()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
