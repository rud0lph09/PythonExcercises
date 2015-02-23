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

#Propuesta: con la misma plantilla anterior de ejemplo, haz que monzi pueda dibujar un poligono de n lados

#Tip: La formula para la suma de todos angulos internos en un poligono de n lados es: (lados -2) * 180


from swampy.TurtleWorld import *			#Importamos el modulo TurtleWorld de swampy

miMundo = TurtleWorld()						#creamos un objeto llamado miMundo de tipo TurtleWorld
monzi = Turtle()							#creamos una tortuga con nombre monzi
lados = 4									#Numero de lados
perimetroTot = 500 							#Esta variable es el valor del perimetro total, esto nos ayuda a no salirnos de la pantalla (es un aprox ya que no estamos usando punto flotante)

def distance(perimetro, nLados):			#Esta funcion recibe dos argumentos, el perimetor y el numero de lados
	largo = perimetro/nLados				#Con esto calcularemos el largo de cada lado para evitar que sea demaciada grande la figura
	return largo							#regresamos el valor de Largo

def angulos(nLados):							#En esta funcion calcularemos la magnitud del angulo a girar con monzi
	angInterno = ((nLados - 2) * 180)/nLados	#esta es la formula para calcular los angulos de un plogono de n lados
	angGiro = 180 - angInterno					#con esta formula obtenemos el angulo con el que giraremos a monzi 
	return angGiro								#esto nos da el valor de retorno del angulo de giro

print monzi									#la ponemos en pantalla

def dibujaTrngl(tortuga, largo, alfa, sides):		#definimos la funcion para dibujar un cuadrado
	for i in range(sides):							#ciclo for para repetir un loop las veces que el poligono tenga lados
		fd(tortuga, largo); lt(tortuga, alfa)		#usamos funcion adelante e izquierda para ir moviendo a la tortuga
													#recordemos que lt tambien puede usar otro parametro el cual es el angulo

dibujaTrngl(monzi, distance(perimetroTot, lados), angulos(lados), lados)	#llamamos la funcion para poder dibujar el cuadrado
																			#le enviamos monzi, lados, angulo y distancia como argumentos
																			#como podemos ver para los angulos le enviamos el valor de 
																			#retorno de la funcion angulos
																			#tambien notar que distance ahora es una funcion que nos regresa
																			#otro valor de retorno
																			#ambos con lados como argumento

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
