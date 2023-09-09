# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
edad = 35
# print es una función
print(edad)
print( type(edad)   )   #  type es una función que nos devuelve el tipo de dato de la variable
nombre_1 = "María Fernanda"
print( type(nombre_1)   )

# 2do ejercicio Realizar un casteo o CONVERSIÓN DEL TIPO DE DATO
nombre_2 = input("\nIngresa tu nombre:\n\n")      #   input es un función
numero= int(input("\nIngresa un número:\n\n"))

# Tipos de datos String - cadena de caracteres

nombre_3 = input("\nIngresa tu nombre:\n\n")
print( type(nombre_3)   )

###########################

# Solicitar el nombre y edad de un usuario
# \n es un salto de línea
nombre_4 = input("\nIngresa tu nombre:\n\n")
edad_2 = int(input("\nIngresa tu edad:\n\n"))
# concatenamos con comas
print("\n\nTu nombre es ",nombre_4," y tienes ",edad_2," años.\n")

###############################
dato = "1234"
print(dato," es de tipo ",type(dato))
# casting cambio de tipo de dato String a int
dato = int(dato)            # conversión EXPLÍCITA del tipo de dato
# el cambio de dato es explícito
print(dato," es de tipo ",type(dato))

# Ejemplo 2
dato = "3.1415"
print(dato," es de tipo ",type(dato))
# convertir a decimal
dato = float(dato)
print(dato," es de tipo ",type(dato))

# CONVERSIÓN IMPLICITA - CASTING
valorUno = 200
valorDos = 300
valorUno = valorUno + valorDos
print( valorUno )

# En Python NO permite concatenar mediante +
##                                   + es únicamente para realizar la operación de suma
valor = 200
valorDos = '400'
print(valor + valorDos)     # va a marcar error

# realizaremos una conversión explícita de int a String
valor = str(valor)
# luego veremos qué sucede si SUMAMOS DOS CADENAS DE CARACTERES
print(valor + valorDos)     # ya NO marca error
# es válido imprimir en pantalla pegaditas las dos variables String

print(valor , valorDos) # ¿Qué sucede si CONCATENAMOS dos cadenas de caracteres?
# R = Nos pone un espacio enmedio

## Tipo de dato qyue sólo arroja Verdadero o Falso ---> Booleano

#                            OPERADORES RELACIONALES
n = 200
n1 = 300
print(n>n1)     # False
print(200==201)     # False
print('Pilares'=='pilares')     # False
print('Pilares'=='Pilares')     # TRUE
print(3.14<=3.142)      # True
print(130%2>2)          # False , operación módulo , cero NO es mayor a 2
# 130/2= 65 y de residuo 0
print(150/2>2)      # True , operación división , 75 sí es mayor a 2
palabra = input("\nIngresa una palabra:\n\n")      # escribimos juan
palabraDos = input("\nIngresa la segunda palabra:\n\n")        # escribimos Juan
print(palabra!=palabraDos)      # True , juan es distinto de Juan

numero = 300
numeroDos = 15
print(numero / numeroDos)
print(numero // numeroDos)      # Operador división entera , revisar las diapositivas

numero = 13
numeroDos = 5       # 13 / 5 = 2.6
print(numero / numeroDos)
print(numero // numeroDos)      # Operador división entera , NO redondea el resultado
# en terminal arroja 2
# en terminal       13 / 5 = 2

# String nombre = "Juan"      # sintáxis ERROR , inválido ya que Python es de tipado dinámico
# por lo que el IDE espera que inicialices tus variables por lo menos
# numeros igual a cero o
# String igual a vacío

# no puedes declarar una variable como lo harías en un lenguaje con tipado estático, es decir,
# una línea de código así:
# String nombre__variable
# es inválido, no le da lectura, marca ERROR, SyntaxError

# print(nombre)         desechamos este Ejemplo desde la línea 97 del código

## OPERADORES LÓGICOS
print((150%2)<(5**2) or (3**2)!=(120%2))        # Si la 1era o 2da expresión lógica resulta Verdadera
# entonces en la terminal va a poner True

# 150/2= 75 , residuo 0 , cero sí es menor a 25 por lo tanto la primera expresión es verdadera
# 120/2= 60 , residuo 0 , 9 sí es distinto a cero  por lo tanto la segunda expresión es verdadera

print((150%2)<(5**2) and (3**2)!=(120%2))        # True

# Soy un comentario para una sola línea
"""
        COMENTARIO EN BLOQUE
        Soy un comentario de varis líneas
        ¿Cuál es la mejor manera de documentar mi código?
        
        ¿con qué tipo de comentario?
        
"""

'''
        SOY UN COMENTARIO DE VARIAS LÍNEAS
'''