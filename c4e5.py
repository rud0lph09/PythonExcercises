# -*- coding: utf-8 -*- 
"""	Rodolfo Castillo Vidrio. 2015. 			Todos los ejercicios desarrollados en este repo se basan en el libro "think python" por Allen Downey.
											Every excercise developed in this repo is based on the book "think python" by Allen Downey.

Español : 	Los ejercicios en este repo, no estaran numerados en base al libro, si no conforme los temas que se vean en cada capítulo
			c# indica el capitulo, e# indica el numero de ejercicio segun MI CUENTA .

English :	This excercises are not named after the excercices of the book but instead are named after the chapters C# marks the chapter
			while e# marks the number of the excercise wich is based entirely on MY OWN COUNT.
			This are scripts to be excecuted by the python translator.
			Definitions and comentaries will be in Spanish. Some terms will be on English. Take this into account if you wish to use my excercises as guides
			The reason to this is because this repo is ment to help students from my College


Instalando Swampy: 	Swampy es una suite creada por Allen Downey, la cual sirve de entorno gráfico y sera necesaria apartir del 4o Capitulo de su libro
					Para revisar si se tiene swampy, ejecutar el interprete de python en consola con el comando "python", posteriormente escribir:

						import swampy.TurtleWorld

					Si no obtienes ningun mensaje de error puedes entonces continuar. De lo contrario es necesario instalar. Ejecuta el siguiente comando
					en consola:

						install pip swampy   		o 			sudo install pip swampy

					Una vez terminado puedes continuar con el capitulo 4

Installing Swampy: 	Please go to: http://thinkpython.om/swampy for instructions on installing swampy


"""

#Propuesta: Conbina todo lo anterior para crear un circulo de radio r
#Tip: La formula del perimetro de el perimetro de un circulo es π*diametro


from swampy.TurtleWorld import *			#Importamos el modulo TurtleWorld de swampy
import math

miMundo = TurtleWorld()						#creamos un objeto llamado miMundo de tipo TurtleWorld
monzi = Turtle()							#creamos una tortuga con nombre monzi
lados = 28.0								#Numero de secciones del circulo
largo = 25.0                                #Largo de cada seccion del circulo

def radio(nSecciones, lSeccion):			#con esta funcion podremos calcular el radio
	perimetro = lSeccion * nSecciones		#utilizamos la formula del perimitro de un poligno
	diametro = perimetro/math.pi 			#posteriormente utilizamos la del perimitro de un circulo y despejamos diametro
	radius = diametro/2.0					#calculamos el radio
	return radius							#y lo mandamos como valor de retorno


def angulos(nLados):								#En esta funcion calcularemos la magnitud del angulo a girar con monzi
	angInterno = ((nLados - 2.0) * 180.0)/nLados	#esta es la formula para calcular los angulos de un plogono de n lados
	angGiro = 180.0 - angInterno					#con esta formula obtenemos el angulo con el que giraremos a monzi 
	return angGiro									#esto nos da el valor de retorno del angulo de giro

print monzi									#la ponemos en pantalla

def dibujaPoly(tortuga, largo, alfa, sides):		#definimos la funcion para dibujar un cuadrado
	pd(tortuga)
	for i in range(int(sides)):							#ciclo for para repetir un loop las veces que el poligono tenga lados
		fd(tortuga, largo); lt(tortuga, alfa)		#usamos funcion adelante e izquierda para ir moviendo a la tortuga
													#recordemos que lt tambien puede usar otro parametro el cual es el angulo

def circulo(radius):			#En esta funcion haremos un circulo, pero primero tenemos que prepararnos
	pu(monzi)					#tenemos que movernos primero la distancia del radio, hacia abajo para comenzar a dibujarlo
	rt(monzi)					#recordemos que siempre se inicia la tortuga volteando a la derecha
	fd(monzi, radius)			#una vez que estamos en posicion la comenzamos a dibujar, para posteriormente regresar
	lt(monzi)					#es importante moverze la mitad del largo de nuestras secciones hacia atras, esto para que el circulo
	pu(monzi)					#quede bien centrado (este comentario no describe cada linea si no la funcion en si)
	bk(monzi, (largo/2))
	dibujaPoly(monzi, largo, float(angulos(float(lados))), lados)	#llamamos la funcion dibuja poli
	fd(monzi, (largo/2))										
	lt(monzi)								#Despues hacemos exactamente lo mismo pero para que la tortuga
	pu(monzi)								#quede centrada
	fd(monzi, radius)

circulo(radio(float(lados), float(largo)))	#llamamos la funcion circulo para realizarlo



print 										#simples print para dejar espacio e imprimir una instruccion al usuario
print
print "El proceso ha terminado, puedes cerrar la ventana de TurtleWorld cuando desees para terminar el programa."
print

wait_for_user()								#esperamos a que el usuario cierre la ventana

print "Hasta luego! :)"						#mensaje de despedida
print


"""
Español: Para ejecutar solo ir a la carpeta (desde la terminal) y ejecutar el comando "python nombre.py" por nombre me refiero al nombre del ejercicio

English: To execute just enter the folder you saved this file (from the terminal) and execute the command "python name.py"
"""
