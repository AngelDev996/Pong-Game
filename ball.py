from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.x_move = 10
        self.y_move = 10


    def mover(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def rebotar(self):
        self.y_move *= -1

    def rebote_en_paddle(self):
        self.x_move *= -1

    def reset_posicion(self):
        self.goto(0,0)
        self.rebote_en_paddle()
