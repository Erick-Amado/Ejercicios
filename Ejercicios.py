===== ERICK DE JESUS AMADO OLVIERA =====
1.- ___________________________________________________________________
def contar(lista):
    ocurrencia = {}
    for palabra in lista:
        if palabra in ocurrencia:
            ocurrencia[palabra] += 1
        else:
            ocurrencia[palabra] = 1
    return ocurrencia
palabras = ["python", "java", "python", "c++"]
resultado = contar(palabras)
print(resultado)


2.- ___________________________________________________________________
def combinar (diccionario1, diccionario2):
    combinacion = diccionario1.copy()
    for clave, valor in diccionario2.items():
        if clave in combinacion:
            combinacion[clave] += valor
        else:
            combinacion[clave] = valor
    return combinacion
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'b': 3, 'c': 4}
resultado = combinar(diccionario1, diccionario2)
print(resultado)

3.- ___________________________________________________________________
def frecnumeros(lista):
    frecuencia = {}
    for numero in lista:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    return frecuencia
numeros = [1, 1, 2, 3, 3, 3]
resultado = frecnumeros(numeros)
print(resultado)

4.- ___________________________________________________________________
def filtrar(lista, longitud):
    return [palabra for palabra in lista if len(palabra) > longitud]
palabras = ["hola", "mundo", "python", "programación"]
longitud = 5
resultado = filtrar(palabras, longitud)
print(resultado) 

5.- ___________________________________________________________________
def invertir(lista):
    return [(b, a) for a, b in lista]
tuplas = [(1, 2), (3, 4), (5, 6)]
resultado = invertir(tuplas)
print(resultado)

6.- ___________________________________________________________________
from collections import Counter

def valoryfrec(lista):
    if not lista:
        return None
    frecuencia = Counter(lista)
    return max(frecuencia, key=frecuencia.get)
numeros = [1, 2, 3, 1, 2, 1]
resultado = valoryfrec(numeros)
print(resultado) 

7.- ___________________________________________________________________
def subconjunto(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2)

conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}
resultado = subconjunto(conjunto1, conjunto2)
print(resultado)

8.- ___________________________________________________________________
def agrupar(personas):
    agrupado = {}
    for persona in personas:
        edad = persona["edad"]
        nombre = persona["nombre"]
        if edad not in agrupado:
            agrupado[edad] = []
        agrupado[edad].append(nombre)
    return agrupado
personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 25}, {"nombre": "Carlos", "edad": 30}]
resultado = agrupar(personas)
print(resultado)


9.- ___________________________________________________________________
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])
    
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado
numeros = [5, 3, 8, 6, 2]
resultado = merge_sort(numeros)
print(resultado)

10.- ___________________________________________________________________
def deletmenores(lista, limite):
    return [x for x in lista if x >= limite]

numeros = [1, 2, 3, 4, 5]
limite = 3
resultado = deletmenores(numeros, limite)
print(resultado) 

11.- ___________________________________________________________________
def aplanar(lista_de_listas):
    return [elemento for sublista in lista_de_listas for elemento in sublista]

lista_de_listas = [[1, 2], [3, 4], [5]]
resultado = aplanar(lista_de_listas)
print(resultado)

12.- ___________________________________________________________________
def calcmediana(lista):
    lista_ordenada = sorted(lista)
    longitud = len(lista)
    mitad = longitud // 2
    
    if longitud % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]

numeros = [1, 3, 2, 4, 5]
resultado = calcmediana(numeros)
print(resultado) 

13.- ___________________________________________________________________
def duplicar(lista):
    return [num for num in lista for _ in range(2)]
numeros = [1, 2, 3]
resultado = duplicar(numeros)
print(resultado) 

14.- ___________________________________________________________________
def contarpalabras(frases):
    return {i: len(frase.split()) for i, frase in enumerate(frases)}

frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
resultado = contarpalabras(frases)
print(resultado)  

15.- ___________________________________________________________________
def cmax(diccionario):
    return max(diccionario, key=diccionario.get)

diccionario = {'a': 10, 'b': 20, 'c': 5}
resultado = cmax(diccionario)
print(resultado) 

16.- ___________________________________________________________________
def palindromos(lista):
    return [palabra for palabra in lista if palabra == palabra[::-1]]

palabras = ["ana", "oso", "hola", "level"]
resultado = palindromos(palabras)
print(resultado)
