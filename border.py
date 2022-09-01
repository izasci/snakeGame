from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-290, 290)
        self.square()

    def square(self):
        self.pendown()
        for i in range(4):
            self.forward(580)
            self.right(90)
