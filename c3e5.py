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


			+ - - - - + - - - - +
			|		  |			|
			|		  |			| 				Este es el ejemplo
			|		  |			|				del cuadrado que se
			|		  |			|				plantea en la 
			+ - - - - + - - - - +				propuesta a realizar
			|		  |			|
			|		  |			|
			|		  |			|
			|		  |			|
			+ - - - - + - - - - +


"""


#Dibuja un cuadrado usando la funcion print

vigas = "|         |         |" 	  	#Solo creamos dos variables string
pisos = "+ - - - - + - - - - +"			#en las que ponemos parte de la figura

def realiza4veces(stringT):				#en esta funcion al declarla especificamos que
	print stringT; print stringT 		#le pasaremos un argumento para repetirlo 
	print stringT; print stringT		#cuatro veces en forma de impresion

def cuadrado():									#Llamamos a print para imprimr los "pisos del cuadrado"
	print pisos; realiza4veces(vigas)			#y luego insertamos el cuerpo con realiza4veces
	print pisos; realiza4veces(vigas)
	print pisos

cuadrado()			#ejecutamos la funcion cuadrado y listo


"""
Español: Para ejecutar solo ir a la carpeta (desde la terminal) y ejecutar el comando "python nombre.py" por nombre me refiero al nombre del ejercicio

English: To execute just enter the folder you saved this file (from the terminal) and execute the command "python name.py"
"""
