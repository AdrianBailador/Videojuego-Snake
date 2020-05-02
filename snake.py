import turtle
import time
import random

#Se ejecute mas lento
posponer = 0.1 


#Creamos una ventana, color, tamaño
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)


#Cabeza de serpiente
cabeza = turtle.Turtle()
cabeza.speed(0) #Cuando inicies la pantalla, la cabeza ya aparezca
cabeza.shape("square") #cabeza sea cuadrada
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
comida.goto(0,100)

#Cuerpo de la serpiente
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




def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y+20)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y-20)

	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x-20)

	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x+20)

#Conectar teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")



while True:
	wn.update()
	if cabeza.distance(comida) < 20:
		x = random.randint(-280,280) 
		y = random.randint(-280,280)
		comida.goto(x,y) #actualizar nuestra posicion

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0) 
		nuevo_segmento.shape("square")
		nuevo_segmento.color("grey")
		nuevo_segmento.penup()
		


	mov()
	time.sleep(posponer)