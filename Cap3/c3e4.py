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
"""

#Propuesta: Crea una funcion que se llame justificadoDer que imprima el nombre de allen letra por letra con un espacio de 13 por letra

print 				#Imprime un espacio

def printSpace():				#esta funcion contine 13 llamadas a print
	print; print; print 		#lo que nos da un espacio de 13 lineas
	print; print; print
	print; print; print
	print; print; print
	print

def justificadoDer(nombre):      		#esta funcion imprime todas las letras del nombre y aparte entre cada una	
	print nombre[0]; printSpace()		#llamamos a la funcion print space
	print nombre[1]; printSpace()
	print nombre[2]; printSpace()
	print nombre[3]; printSpace()
	print nombre[4]; printSpace()

justificadoDer('Allen')					#Llamamos a la funcion de justificado ara posteriormente
										#enviarle el argumento de allen

"""
Español: Para ejecutar solo ir a la carpeta (desde la terminal) y ejecutar el comando "python nombre.py" por nombre me refiero al nombre del ejercicio

English: To execute just enter the folder you saved this file (from the terminal) and execute the command "python name.py"
"""
