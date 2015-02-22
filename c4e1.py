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

#En esta ocacion probaremos el modulo de Turtle World que forma parte de Swampy el cual es un paquete.

from swampy.TurtleWorld import *

world = TurtleWorld() 	#inicializa el entorno grafico de TurtleWorld
bob = Turtle()			#asignamos la bariable bob como objeto de tipo Turtle
print bob				#imprimimos a bob en la pantalla del entorno gráfico

for i in range(4):		#este es un ciclo for, el cual provocara que se repita el bloque de codigo en su interior
						#cuatro veces
	fd(bob, 100)		#esta funcion fd nos permite mover a bob hacia adelante, para atras seria bk
	lt(bob)				#esta funcion nos permite voltear a bob a la izquierda

	#con este codigo creamos un cuadrado

wait_for_user() 		#esperamos al usuario para que pueda ver el resultado

"""
Español: Para ejecutar solo ir a la carpeta (desde la terminal) y ejecutar el comando "python nombre.py" por nombre me refiero al nombre del ejercicio

English: To execute just enter the folder you saved this file (from the terminal) and execute the command "python name.py"
"""
