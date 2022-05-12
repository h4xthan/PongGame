import turtle

#Ventana
wn = turtle.Screen()
wn.title("Pong by Nesx")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Marcador
marcadorA = 0
marcadorB = 0

#Jugador A
JugadorA = turtle.Turtle()
JugadorA.speed(0)
JugadorA.shape("square")
JugadorA.color("white")
JugadorA.penup()
JugadorA.goto(-350,0)
JugadorA.shapesize(stretch_wid=5, stretch_len=1)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.1
pelota.dy = 0.1

#Jugador B
JugadorB = turtle.Turtle()
JugadorB.speed(0)
JugadorB.shape("square")
JugadorB.color("white")
JugadorB.penup()
JugadorB.goto(350,0)
JugadorB.shapesize(stretch_wid=5, stretch_len=1)

#Linea Division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("JugadorA : 0         JugadorB: 0", align = "center", font =("Courier", 24, "normal"))

#Funciones
def JugadorA_up():
    y = JugadorA.ycor()
    y += 20
    JugadorA.sety(y)
def JugadorA_down():
    y = JugadorA.ycor()
    y -= 20
    JugadorA.sety(y)
def JugadorB_up():
    y = JugadorB.ycor()
    y += 20
    JugadorB.sety(y)
def JugadorB_down():
    y = JugadorB.ycor()
    y -= 20
    JugadorB.sety(y)

#Teclado    
wn.listen()
wn.onkeypress(JugadorA_up, "w")
wn.onkeypress(JugadorA_down, "s")
wn.onkeypress(JugadorB_up, "Up")
wn.onkeypress(JugadorB_down, "Down")


while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)


    #Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    #Bordes derecha/izquierda
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("JugadorA : {}         JugadorB: {}".format(marcadorA, marcadorB), align = "center", font =("Courier", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("JugadorA : {}         JugadorB: {}".format(marcadorA, marcadorB), align = "center", font =("Courier", 24, "normal"))

    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and(pelota.ycor() < JugadorB.ycor() + 50
            and pelota.ycor() > JugadorB.ycor() -50)):
            pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and(pelota.ycor() < JugadorA.ycor() + 50
            and pelota.ycor() > JugadorA.ycor() - 50)):
        pelota.dx *= -1
