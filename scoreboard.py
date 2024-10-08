from turtle import Turtle

FONT = ("arial",24, "normal")
ALIGNMENT = "center"

// managing scoreboard

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open("data.txt.py") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_scorecard()


    def update_scorecard(self):
        self.clear()
        self.write(f"score:{self.score}  highscore:{self.high_score}", align=ALIGNMENT,font=FONT)


    def reset(self):

        if self.score >= self.high_score:
            self.high_score = self.score
            with open("data.txt.py", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scorecard()

    def increase_score(self):
        self.score += 1
        self.update_scorecard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT,font=FONT)

