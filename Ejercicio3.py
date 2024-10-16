# 1. Inicializa una variable entera y muestra su valor
entero = 5
print(entero)
print ("------------------------------------------")

# 2. Inicializa una variable de punto flotante y muestra su valor
floatante = 3.14
print(floatante)
print ("------------------------------------------")

# 3. Inicializa una cadena y muestra su longitud
cadena = "Python"
print(len(cadena))
print ("------------------------------------------")

# 4. Inicializa una lista y muestra su primer elemento
lista = [1, 2, 3]
print(lista[0])
print ("------------------------------------------")

# 5. Inicializa un diccionario y muestra un valor por clave
diccionario = {'a': 1, 'b': 2}
print(diccionario['a'])
print ("------------------------------------------")

# 6. Comprobar si un número es par
num = 4
if num % 2 == 0:
    print("Es par") 
else:
    print("Es impar")
print ("------------------------------------------")

# 7. Verificar si una cadena contiene una subcadena
cadena = "Hola Mundo"
if "Mundo" in cadena:
    print("Contiene 'Mundo'")
print ("------------------------------------------")

# 8. Clasificar un número como positivo, negativo o cero
num = -1
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Cero")
print ("------------------------------------------")

# 9. Comprobar si un año es bisiesto
año = 2020
if (año % 4 == 0 and año % 100) or (año % 400 == 0):
    print("Bisiesto")
else:
    print("No bisiesto")
print ("------------------------------------------")

# 10. Validar un número de rango
num = 15
if 1 <= num <= 10:
    print("En rango")
else:
    print("Fuera de rango")
print ("------------------------------------------")

# 11. Imprimir números del 1 al 5 usando un bucle for
for i in range(1, 6):
    print(i, end=", ")
print()
print ("------------------------------------------")

# 12. Sumar los primeros 10 números naturales
suma = sum(range(1, 11))
print(suma)
print ("------------------------------------------")

# 13. Crear una lista con los cuadrados de los primeros 5 números
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)
print ("------------------------------------------")

# 14. Contar cuántas vocales hay en una cadena
cadena = "Hola"
vocales = sum(1 for letra in cadena.lower() if letra in "aeiou")
print(vocales)
print ("------------------------------------------")

# 15. Imprimir una tabla de multiplicar (del 3)
for i in range(1, 11):
    print(3 * i, end=", ")
print()
print ("------------------------------------------")

# 16. Agregar elementos a una lista
lista = []
lista.append(1)
print(lista)  
lista.append(2)
print(lista)
print ("------------------------------------------")

# 17. Crear un conjunto y verificar si un elemento está presente
conjunto = {1, 2, 3}
print(2 in conjunto)
print ("------------------------------------------")

# 18. Crear un diccionario y agregar un par clave-valor
diccionario = {}
diccionario['a'] = 1
print(diccionario)
print ("------------------------------------------")

# 19. Ordenar una lista
lista = [3, 1, 2]
lista.sort()
print(lista)
print ("------------------------------------------")

# 20. Obtener la longitud de una lista
lista = [1, 2, 3]
print(len(lista))
print ("------------------------------------------") 

# 21. Sumar elementos de una lista
lista = [1, 2, 3, 4, 5]
suma = sum(lista)
print(suma)
print ("------------------------------------------")

#22. Filtrar numeros pares de una lista
lista = [1, 2, 3, 4, 5]
pares = [num for num in lista if num % 2 == 0]
print(pares)
print ("------------------------------------------")

#23
cadena = "hola mundo"
print(len(cadena))
print ("------------------------------------------")

#24
list = [1, 2, 3]
val_max = max(list)
print(val_max)
print ("------------------------------------------")

#25
print ("------------------------------------------")
def eliminar_elemento(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
    return diccionario

diccionario = {"nombre": "Juan", "edad": 30}
resultado = eliminar_elemento(diccionario, "edad")
print(resultado) 

#26
print ("26------------------------------------------")

for i in range(1, 6):
    print(i ** 2)

#27
print ("------------------------------------------")
def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

resultado = fibonacci(10)
print(resultado) 

#28
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista_de_tuplas = list(zip(lista1, lista2))
print(lista_de_tuplas)
print ("------------------------------------------")

#29
list = [1, 2, 1, 3]
caracter = 1
Contar = list.count(caracter)
print(Contar)
print ("------------------------------------------")

#30
print ("------------------------------------------")
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

resultado = primo(7)
print(resultado)  

#31
list = [1, 2, 3]
reverse = list[::-1]
print(reverse)
print ("------------------------------------------")

#32
list1 = [1,2]
list2 = [3,4]
list3 = list1 + list2
print (list3)
print ("------------------------------------------")

#33
from random import randint
random = randint(1,10)
list = [random, random, random, random, random]
print(list)
print ("------------------------------------------")

#34
conjunto = {1, 2, 3}
Contar = len(conjunto)
print(Contar)
print ("------------------------------------------")

#35
print ("------------------------------------------")

palabras = ["Hola", "mundo"]
resultado = " ".join(palabras)
print(resultado)  

#36
lista = [1, 2, 2, 3]
unicos = list(set(lista))
print(unicos)
print ("------------------------------------------")

#37
print ("------------------------------------------")
conjunto1 = {'a', 'b', 'c'}
conjunto2 = {'c', 'd', 'e'}
resultado = conjunto1.union(conjunto2)
print(resultado)  

#38
print ("------------------------------------------")
conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
resultado = conjunto1.intersection(conjunto2)
print(resultado)  # Resultado: {2, 3}

#39
print ("------------------------------------------")

mi_diccionario = {"a": 1, "b": 2}

for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")

#40
diccionario = {'a': 1, 'b': 2}
claves = list(diccionario.keys())
valores = list(diccionario.values())
print(claves)
print(valores)
print ("------------------------------------------")

#41
import random

def generar_numeros_aleatorios(cantidad, inicio, fin):
    return [random.randint(inicio, fin) for _ in range(cantidad)]
resultado = generar_numeros_aleatorios(10, 1, 100)
print(resultado)

#42
numeros = [5, 3, 1, 4, 2]
numeros.sort()
print(numeros)

#43.
print ("------------------------------------------")
def contador(cadena):
    palabras = cadena.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

cadena = "Hola mundo hola"
resultado = contador(cadena)
print(resultado) 

#44.
print ("------------------------------------------")

def elementos(lista1, lista2):
    return list(set(lista1) & set(lista2))
lista1 = [1, 2, 3]
lista2 = [2, 3, 4]
resultado = elementos(lista1, lista2)
print(resultado) 

#45
print ("------------------------------------------")

def subconjunto(lista1, lista2):
    return set(lista1).issubset(set(lista2))

lista1 = [1, 2]
lista2 = [1, 2, 3]
resultado = subconjunto(lista1, lista2)
print(resultado)  

#46.
print ("------------------------------------------")
def pares():
    return [x for x in range(1, 21) if x % 2 == 0]

resultado = pares()
print(resultado)  

#47.
print ("------------------------------------------")
def frecuencias(lista):
    conteo = {}
    for num in lista:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1
    return conteo

lista = [1, 2, 2, 3]
resultado = frecuencias(lista)
print(resultado)  

# 48. Unir dos listas alternando sus elementos
print ("------------------------------------------")

def unir(lista1, lista2):
    return [elemento for par in zip(lista1, lista2) for elemento in par]


lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = unir(lista1, lista2)
print(resultado)  

# 49. Encontrar el índice de un elemento en una lista
print ("------------------------------------------")
def encontrar (lista, valor):
    if valor in lista:
        return lista.index(valor)
    else:
        return -1 

lista = [1, 2, 3]
valor = 2
indice = encontrar (lista, valor)
print(f"El valor de {valor} es el índice {indice}")  

#50.Crear un diccionario a partir de una lusta de claves y valores
print ("------------------------------------------")
def creardic(claves, valores):
    return dict(zip(claves, valores))

claves = ['a', 'b']
valores = [1, 2]
resultado = creardic(claves, valores)
print(resultado) 

#51. Filtrar palabras largas de una lista
print ("------------------------------------------")
def filtrarpalabras (palabras):
    return [palabra for palabra in palabras if len(palabra) > 4]

palabras = ["uno", "dos", "tres", "cuatro"]
resultado = filtrarpalabras (palabras)
print(resultado)  

#52.Crear una lista de los índices de los elementos en una lista
print ("------------------------------------------")
def obtindi(lista):
    return list(range(len(lista)))

lista = [10, 20, 30]
resultado = obtindi(lista)
print(resultado)  

#53 Ordenar un diccionario por sus valores
print ("------------------------------------------")

def ordenar (diccionario):
    return dict(sorted(diccionario.items(), key=lambda item: item[1]))

diccionario = {'a': 3, 'b': 1, 'c': 2}
resultado = ordenar (diccionario)
print(resultado) 

#54. Verificar si dos listas son iguales
print ("------------------------------------------")
def listigual(lista1, lista2):
    return lista1 == lista2

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
resultado = listigual(lista1, lista2)
print (resultado)

#55. Crear un conjunto a partir de una lista con duplicados
print ("------------------------------------------")
def conjunto(lista):
    return set(lista)

lista = [1, 1, 2, 3]
resultado = conjunto(lista)
print(resultado)  

#56. Calcular el promedio de una lista
print ("------------------------------------------")
def promedio(lista):
    return sum(lista) / len(lista)

lista = [1, 2, 3, 4, 5]
resultado = promedio(lista)
print(resultado)  

#57.Comprobar si una lista está vacía
print ("------------------------------------------")
def listvacioa(lista):
    return len(lista) == 0


lista = []
resultado = listvacioa(lista)
print(resultado)  

#58. Obtener los elementos únicos de una lista manteniendo el orden
print ("------------------------------------------")
def obtener(lista):
    unicos = []
    for elemento in lista:
        if elemento not in unicos:
            unicos.append(elemento)
    return unicos


lista = [1, 2, 2, 3]
resultado = obtener(lista)
print(resultado) 

#59. Contar las letras en una cadena
print ("------------------------------------------")
def contarlet(cadena):
    conteo = {}
    for letra in cadena:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    return conteo

cadena = "Hola"
resultado = contarlet(cadena)
print(resultado)  

#60. Cambiar el valor de un elemento en un diccionario
print ("------------------------------------------")

def cambiar(diccionario, clave, nuevo_valor):
    diccionario[clave] = nuevo_valor
    return diccionario

diccionario = {'a': 1}
diccionario_actualizado = cambiar(diccionario, 'a', 2)
print(diccionario_actualizado)  

# 61. Eliminar un elemento de una lista
print ("------------------------------------------")
def eliminar(lista, elemento):
    lista.remove(elemento)
    return lista


lista = [1, 2, 3]
resultado = eliminar(lista, 2)
print(resultado)  

#62. Repetir una cadena varias veces
print ("------------------------------------------")
def repetir(cadena, veces):
    return cadena * veces

cadena = "Hola"
resultado = repetir(cadena, 3)
print(resultado)  

#63. Crear una lista de números aleatorios y ordenarla
print ("------------------------------------------")
import random

def listaordenada():
    lista = [random.randint(1, 100) for _ in range(10)]
    lista.sort()
    return lista

resultado = listaordenada()
print(resultado)  

#64. Crear una lista de listas
print ("------------------------------------------")
def crear_listas():
    return [[1, 2], [3, 4]]

resultado = crear_listas()
print(resultado)  




