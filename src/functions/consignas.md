# Functions.py
> Lo único obligario es la función con el mísmo nombre que la consigna. 
> Y esa función debe retornar el resultado esperado.

## exercise_one
> Escribir una función que muestre por pantalla
> el saludo "¡Hola mundo!", cada vez que se la invoque.

## exercise_two
> Escribir una función a la que se le pase una cadena
> <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

## exercise_tree
> Escribir una función que calcule el total de una factura tras aplicarle el IVA.
> La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
> devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

## exercise_four
> Escribir una función que calcule el área de un círculo y otra que calcule el
> volumen de un cilindro usando la primera función.

## exercise_five
> Escribir una función que reciba una muestra de números en una lista y devuelva su promedio.

## exercise_six
> Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

## exercise_seven
> Escribir un programa que reciba una cadena de caracteres y devuelva 
> un diccionario con cada palabra que contiene y su frecuencia.

# Functional

## Carrito
> Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
> Escribir una tercera función que reciba un diccionario con los precios y porcentajes del carrito de la compra, 
> y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA
> a los productos del carrito y devolver el precio final del carrito.

## Calculadora científica
> Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, 
> tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, 
> y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el 
> resultado de aplicar la función a esos enteros.

## Función como parámetro
> Escribir una función que reciba otra función y una lista, 
> y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
> La función que llega por parámetro deberá multiplicar cada número por dos.

## Inmobiliaria
> Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
`
[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
`
> Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
> La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista
> con los inmuebles cuyo precio sea menor o igual que el dado. 
> Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario 
> con el precio del inmueble, donde el precio de un inmueble se calcula con la siguiente fórmula en 
> función de la zona:
> Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
> Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5