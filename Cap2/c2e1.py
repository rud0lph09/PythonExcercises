# -*- coding: utf-8 -*- 
"""	Rodolfo Castillo Vidrio. 2015. 			Todos los ejercicios desarrollados en este repo se basan en el libro "think python" por Allen Downey.
											Every excercise developed in this repo is based on the book "think python" by Allen Downey.

Español : 	Los ejercicios en este repo, no estaran numerados en base al libro, si no conforme los temas que se vean en cada capítulo
			c# indica el capitulo, e# indica el numero de ejercicio segun MI CUENTA.
			Este ejercicio es el que se puede encontrar al final en la pag 9 del primer capítulo

English :	This excercises are not named after the excercices of the book but instead are named after the chapters C# marks the chapter
			while e# marks the number of the excercise wich is based entirely on MY OWN COUNT.
			This are scripts to be excecuted by the python translator.
			Definitions and comentaries will be in Spanish. Some terms will be on English. Take this into account if you wish to use my excercises as guides
			The reason to this is because this repo is ment to help students from my College
"""

#Propuesta: utilizando la formula de volumen de la esfera 4/3π * (r al cubo), r siendo el radio. ¿Cuál sera el volumen de una esfera con radio 5.

print 'Calculando el volumen de una esfera de radio 5 es: ' #mensaje para el usuario acerca de la propuesta

pi = 3.141592							#valor aproximado de π
radius = 5.0							#valor del radio
sqrRadius = radius*radius 			#valor del radio al cuadrado
vol = (3.0/4.0)*pi*sqrRadius			#formula para el calculo de volumen

print vol 								#imprimimos volumen
print 'unidades cuadradas'				#aclaramos unidades

"""
Español: Para ejecutar solo ir a la carpeta (desde la terminal) y ejecutar el comando "python nombre.py" por nombre me refiero al nombre del ejercicio

English: To execute just enter the folder you saved this file (from the terminal) and execute the command "python name.py"
"""


