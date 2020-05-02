import turtle
import time
import random

#Se ejecute mas lento
posponer = 0.1 

#Marcador
score = 0
high_score = 0


#Creamos una ventana, color, tamaño
wn = turtle.Screen()
wn.title("Juego de Snake, Adrián BP")
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

#Texto
texto = turtle.Turtle()
texto.speed(0) #El texto aparezca pintado en la pantalla
texto.color("white")
texto.penup() #No aparezca la pluma que pinta nuestro texto
texto.hideturtle() #Esconder la pluma
texto.goto(0,260) #parte superior
texto.write("Score: 0        High Score: 0", align = "center", font = ("Courier",24,"normal"))


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

	#Chocar contra los bordes
	if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"

		#Esconder los segmentos

		for segmento in segmentos:
			segmento.goto(1000,1000)

		#limpiar la lista de segmentos
		segmentos.clear()

		#Resetear Marcador
		score = 0
		texto.clear()	
		texto.write("Score: {}    High Score: {}".format(score,high_score),
		 align = "center", font = ("Courier",24,"normal")) 

	if cabeza.distance(comida) < 20:
		x = random.randint(-280,280) 
		y = random.randint(-280,280)
		comida.goto(x,y) #actualizar nuestra posicion

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0) 
		nuevo_segmento.shape("square")
		nuevo_segmento.color("grey")
		nuevo_segmento.penup()
		segmentos.append(nuevo_segmento)

		#Aumentar Marcador
		score += 10

		if score > high_score:
			high_score = score

		texto.clear()	
		texto.write("Score: {}    High Score: {}".format(score,high_score),
		 align = "center", font = ("Courier",24,"normal")) 


		
	#Mover el cuerpo de la serpiente	
	totalSeg = len(segmentos)
	for index in range(totalSeg -1, 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x,y)


	#coordenadas de la cabeza	
	if totalSeg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		segmentos[0].goto(x,y)
		


	mov()

	#Colisiones Cuerpo
	for segmento in segmentos:
		if segmento.distance(cabeza) < 20:
			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction = "stop"

		
			#Esconder los segmentos
			for segmento in segmentos:
				segmento.goto(1000,1000)

			#limpiar la lista de segmentos
			segmentos.clear()

			#Resetear Marcador
			score = 0
			texto.clear()	
			texto.write("Score: {}    High Score: {}".format(score,high_score),
		 	align = "center", font = ("Courier",24,"normal")) 

	time.sleep(posponer)