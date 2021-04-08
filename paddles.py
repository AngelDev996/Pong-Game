from turtle import Turtle


class Paddles(Turtle):

    def __init__(self, posicion):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posicion)

    def mover_arriba(self):
        nueva_y = self.ycor() + 20
        self.goto(self.xcor(), nueva_y)

    def mover_abajo(self):
        nueva_y = self.ycor() - 20
        self.goto(self.xcor(), nueva_y)
