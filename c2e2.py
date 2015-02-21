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

#Suponiendo que el costo de un libro que se busca adquirir en la biblioteca es de 24.95 dolares, la biblioteca de la universidad tiene un 40% de descuento.
#el costo de envio es de 3 dolares por el primer ejemplar y 75 centavos de dolar por cada copia adicional. Tomando el precio del dolar como 15 pesos mexicanos
#¿Cuál es el costo total por 60 copias del libro? Imprimir el resultado en dolares y posteriormente en pesos.


bookPrice = 24.95					#costo del libro
numItems = 60.0						#numero de libros a comprar
bulkPrice = numItems * bookPrice 	#valor crudo de todos los libros: multiplicamos el costo del libro por la cantidad a comprar
shipCost = 3.0 						#costo de entrega de un ejemplar
addShipCost = 0.75					#costo de entrega de ejemplares adicionales	
discount = 0.60						#descuento universitario 100% - 40% = 60%... Por lo tanto el valor es de .6		

totalShipCost = shipCost + (addShipCost * (numItems - 1))  		#primero calculamos el costo de envio
parcTotal = bulkPrice * discount								#calculamos el total parcial con descuento
total = parcTotal + totalShipCost								#calculamos el precio total sumando el parcial a el costo de entrega total

print 'Detalles de costos en dolares...'
print 'costo de envio:'
print totalShipCost
print 'costo del pedido con descuento:'
print parcTotal 
print 'total a pagar:'
print total
print 'Detalles de costos en pesos...'
print 'costo de envio:'
print totalShipCost * 15
print 'costo del pedido con descuento:'
print parcTotal * 15
print 'total a pagar:'
print total * 15

"""
Español: Para ejecutar solo ir a la carpeta (desde la terminal) y ejecutar el comando "python nombre.py" por nombre me refiero al nombre del ejercicio

English: To execute just enter the folder you saved this file (from the terminal) and execute the command "python name.py"
"""


