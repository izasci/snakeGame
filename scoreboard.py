from turtle import Turtle
STARTING_SCORE = 0
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = STARTING_SCORE
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 270)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.home()
        self.write(arg=f"   GAME OVER\nYour score is: {self.score}", move=False, align=ALIGNMENT, font=FONT)
