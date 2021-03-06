# -*- coding: utf-8 -*- 
"""	Rodolfo Castillo Vidrio. 2015. 			Todos los ejercicios desarrollados en este repo se basan en el libro "think python" por Allen Downey.
											Every excercise developed in this repo is based on the book "think python" by Allen Downey.

Español : 	Los ejercicios en este repo, no estaran numerados en base al libro, si no conforme los temas que se vean en cada capítulo
			c# indica el capitulo, e# indica el numero de ejercicio segun MI CUENTA a menos que .
			Este ejercicio es el que se puede encontrar al final en la pag 9 del primer capítulo

English :	This excercises are not named after the excercices of the book but instead are named after the chapters C# marks the chapter
			while e# marks the number of the excercise wich is based entirely on MY OWN COUNT.
			This are scripts to be excecuted by the python translator.
			Definitions and comentaries will be in Spanish. Some terms will be on English. Take this into account if you wish to use my excercises as guides
			The reason to this is because this repo is ment to help students from my College
"""


#Propuesta: Si me voy a las 6:52 am a correr y llevo un ritmo relajado durante la primera milla (8:52mins por Milla) y luego corro 3 a un ritmo de (7:12min por Milla)
#			y por ultimo corro 1 milla mas al ritmo relajado. ¿Cuanto tiempo tardare?


millas = 5.0
milRelax = 2.0
milForte = 3.0
ritRelax = 8.0 + (52.0/60.0)
ritForte = 7.0 + (12.0/60.0)

timRelax = milRelax * ritRelax
timForte = milForte * ritForte

timTotal = timForte + timRelax

print "regresaras a casa en: " 
print timTotal 
print "minutos"


"""
Español: Para ejecutar solo ir a la carpeta (desde la terminal) y ejecutar el comando "python nombre.py" por nombre me refiero al nombre del ejercicio

English: To execute just enter the folder you saved this file (from the terminal) and execute the command "python name.py"
"""
