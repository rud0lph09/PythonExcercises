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

#Ejemplo del codigo de funciones en el capitulo 3. Pagina 22


def printLyrics():											#Como en el ejercicio anterior declaramos una funcion
	print "En una fuente, habia un chorrito"				#escribimos el codigo que se ejecutara
	print "se hacia grandote, se hacia chiquito"			#al llamar la funcion

def repeatLyrics():						#Declaramos otra funcion
	printLyrics()						#llamamos la funcion anterior
	printLyrics()

repeatLyrics()			#Como en esta funcion al declarla su codigo llama dos veces a la funcion
						#Printlyrics entonces esa funcion se repetira dos veces, pero en realidad solo llamamos
						#una vez a repeat Lyrics

"""
Español: Para ejecutar solo ir a la carpeta (desde la terminal) y ejecutar el comando "python nombre.py" por nombre me refiero al nombre del ejercicio

English: To execute just enter the folder you saved this file (from the terminal) and execute the command "python name.py"
"""
