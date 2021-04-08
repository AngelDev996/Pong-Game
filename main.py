from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

pantalla = Screen()

pantalla.setup(width=800, height=600)
pantalla.bgcolor("black")
pantalla.title("Pong")

pantalla.tracer(0)  # Esta linea deshabilita toda animacion, incluso los elementos de la pantalla

l_paddle = Paddles((-350, 0))
r_paddle = Paddles((350, 0))

pantalla.listen()

pantalla.onkey(r_paddle.mover_arriba, "Up")
pantalla.onkey(r_paddle.mover_abajo, "Down")
pantalla.onkey(l_paddle.mover_arriba, "w")
pantalla.onkey(l_paddle.mover_abajo, "s")

pelota = Ball()
score = Scoreboard()
detectar_colision = False
juego_encendido = True

sleep_time = 0.1
while juego_encendido:
    if sleep_time == 0:
        sleep_time = 0.01
    time.sleep(sleep_time)
    pantalla.update()  # Esta linea actualiza la pantalla y sus elementos
    pelota.mover()

    # Deteccion de la bola con la pared vertical superior o inferior
    if pelota.ycor() == 290 or pelota.ycor() == -290:
        pelota.rebotar()

    # Deteccion de la bola con los paddles
    if pelota.distance(r_paddle) < 20 and pelota.xcor() > 340 or pelota.distance(
            l_paddle) < 20 and pelota.xcor() < -340:
        pelota.rebote_en_paddle()
        sleep_time -= 0.01


    # Deteccion si el paddle derecho falla la bola
    if pelota.xcor() > 380:
        score.punto_l()
        pelota.reset_posicion()
        sleep_time=0.1

    # Deteccion si el paddle izquierdo falla la bola
    if pelota.xcor() < -380:
        score.punto_r()
        pelota.reset_posicion()
        sleep_time=0

pantalla.exitonclick()
