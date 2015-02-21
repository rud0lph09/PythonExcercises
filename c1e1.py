#	Rodolfo Castillo Vidrio. 2015. 			Todos los ejercicios desarrollados en este repo se basan en el libro "think python" por Allen Downey.
#											Every excercise developed in this repo is based on the book "think python" by Allen Downey.

#Español : 	Los ejercicios en este repo, no estaran numerados en base al libro, si no conforme los temas que se vean en cada capítulo
#			c# indica el capitulo, e# indica el numero de ejercicio segun MI CUENTA.
#			Es importante tomar en cuenta que los ejercicios aqui son scripts, para ser ejecutados por el interpreter, por lo tanto
#			no desplegara informacion al realizar las operaciones.
#			Este ejercicio es el que se puede encontrar al final en la pag 9 del primer capítulo

#English :	This excercises are not named after the excercices of the book but instead are named after the chapters C# marks the chapter
#			while e# marks the number of the excercise wich is based entirely on MY OWN COUNT.
#			This are scripts to be excecuted by the python translator.
#			This excercise is based on the proposed one from page 9 chapter 1, but also takes variables into account. The full topic of variables
#			Can be seen on chapter 2
#			Definitions and comentaries will be in Spanish. Some terms will be on English. Take this into account if you wish to use my excercises as guides
#			The reason to this is because this repo is ment to help students from my College


#Propuesta: Un objeto se desplaza 10 kilometros durante 43 minutos con 30 segundos.
#			¿Cual sera su velocidad en millas por hora?



dist = 10.0						#distancia en kilometros 			
kInM = 1.61						#cantidad de kilometrols en una milla
time = 43.0						#solo el tiempo en minutos
exSec = 30.0					#el tiempo restante en segundos
SecInH = 3600.0					#cantidad de segundos en una hora
vel = 0.0						#declaracion de la variable de velocidad

dist = dist / kInM				#primero transformamos la distancia de kilometros a millas
time = time * 60.0				#despues transformamos los minutos a segundos
time = time + exSec  			#le añadimos los segundos extras
time = time / SecInH			#posteriormente transformamos todos los segundos a horas
								#usando el factor de conversion de segundos en horas

vel = dist / time				#efectuamos la formula de velocidad

print  vel 						#imprimimos la variable de velocidad
print ("miles per hour")		#aclaramos las unidades en las que estaran


#Español: Para ejecutar solo ir a la carpeta (desde la terminal) y ejecutar el comando "python nombre.py" por nombre me refiero al nombre del ejercicio

#English: To execute just enter the folder you saved this file (from the terminal) and execute the command "python name.py"