from turtle import Turtle
STARTING_SCORE = 0
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')
with open("high_score.txt", mode="r") as file:
    file_with_hs = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = STARTING_SCORE
        with open("high_score.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.home()
    #     self.write(arg=f"   GAME OVER\nYour score is: {self.score}", move=False, align=ALIGNMENT, font=FONT)
