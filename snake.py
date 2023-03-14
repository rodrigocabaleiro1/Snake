import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0

#Configuración de la ventana
wn= turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width = 500, height = 500)
wn.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,200)

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,220)
texto.write("Score: 0       High Score: 0", align = "center", font = ("Courier", 18, "normal"))

#Segmentos / Cuerpo de la serpiente
segmentos = []

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"
#def close():
 #   wn.close()
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)


    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
def gameover():
    time.sleep(1)
    cabeza.goto(0,0)
    cabeza.direction = "stop"

    #Esconder segmentos
    for segmento in segmentos:
        segmento.goto(1000,1000)

    #Eliminar segmentos
    segmentos.clear()

    #Resetear marcador
    score = 0
    texto.clear()
    texto.write("Score: {}       High Score: {}".format(score,high_score), align = "center", font = ("Courier", 18, "normal"))

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
#wn.onkeypress(close, "Scape")

while True:
    wn.update()

    #Colisiones bordes
    if cabeza.xcor() > 240 or cabeza.xcor()< -240 or cabeza.ycor() > 240 or cabeza.ycor() < -240:
        gameover()

    #Colision con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            gameover()


    #Colisiones comida
    if cabeza.distance(comida) < 20:
        x= random.randint(-210,210)
        y= random.randint(-210,210)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        score += 10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score,high_score), align = "center", font = ("Courier", 18, "normal"))

    #Mover el cuerpo de la serpiente
    totalseg = len(segmentos)
    for index in range(totalseg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()
    time.sleep(posponer)


