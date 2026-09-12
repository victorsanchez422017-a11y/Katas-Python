# 1.Escribe una función que reciba una cadena de texto como
# parámetro y devuelva un diccionario con las frecuencias 
# de cada letra en la cadena. Los espacios no deben ser 
# considerados

def contar_letras(texto):
    frecuencias = {}
    for letra in texto.lower():
        if letra == " ":
            continue
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias
print(contar_letras("the power data analytics"))
# La letra que más se repite es la a, 4 veces, seguida 
# de la t, que se repite 3 

#----------------------------------------------------------

# 2.Dada una lista de números, obtén una nueva lista con el 
# doble de cada valor. Usa la función map()

numeros = [1, 2, 3, 4, 5, 6]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles) # Resultado [2, 4, 6, 8, 10, 12]

#----------------------------------------------------------

# 3. Escribe una función que tome una lista de palabras
# y una palabra objetivo como parámetros. La función
# debe devolver una lista con todas las palabras de 
# la lista original que contengan la palabra objetivo

def filtrar_palabras(lista_palabras, palabra_objetivo):
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]
# Por ejemplo
palabras = ["casa", "casita", "perro", "gato", "casas", "árbol"]
objetivo = "casa"
resultado = filtrar_palabras(palabras, objetivo)
print(resultado) # casita no tiene la palabra "casa" dentro, 
                 # por eso al filtrar no aparece 

#----------------------------------------------------------

# 4. Genera una función que calcule la diferencia 
# entre los valores de dos listas. Usa la función map()
def calcular_diferencia(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

# Por ejemplo
lista1 = [10, 20, 30, 40]
lista2 = [1, 12, 23, 34]

resultado = calcular_diferencia(lista1, lista2)
print(resultado)  # El resultado es [9, 8, 7, 6]

#----------------------------------------------------------

# 5. Escribe una función que tome una lista de números como
# parámetro y un valor opcional nota_aprobado, que por 
# defecto es 5. La función debe calcular la media de los 
# números en la lista y determinar si la media es mayor o 
# igual que nota aprobado. Si es así, el estado será
# "aprobado", de lo contrario, será "suspenso". La función 
# debe devolver una tupla que contenga la media y el estado

def evaluar_notas(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# Un ejemplo de un aprobado 
notas = [7, 6, 8 ]
resultado = evaluar_notas(notas)
print(resultado)  # (6.8, 'aprobado')

# Un ejemplo de un suspenso
notas2 = [5, 4, 3.1 , 7.5]
resultado2 = evaluar_notas(notas2, nota_aprobado=6)
print(resultado2)  # (4.9, 'suspenso')

#----------------------------------------------------------

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print (factorial(3)) # Devuelve 6
print (factorial(-3)) # Devuelve "El factorial no está definido para números negativos"

#----------------------------------------------------------

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. 
# Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))

tuplas = [(4 , 5), ('hola', 'adiós')]
resultado_string = tuplas_a_strings(tuplas)
print(resultado_string) # Devuelve ['(4, 5)', "('hola', 'adiós')"] como string 

#----------------------------------------------------------

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. 
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja
# esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
# indicando si la división fue exitosa o no.

def dividir_numeros():
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 / numero2
    except ValueError:
        print(" Error: debe insertar un valor numérico válido. ")
    except ZeroDivisionError:
        print(" Error: no se puede dividir entre cero. Inserte otro número")
    else:
        print(f" División exitosa: {numero1} / {numero2} = {resultado}")

dividir_numeros()

# Ingrese el primer número: 1
# Ingrese el segundo número: 34
# División exitosa: 1.0 / 34.0 = 0.029411764705882353

# Ingrese el primer número: -1
# Ingrese el segundo número: 0
# Error: no se puede dividir entre cero. Inserte otro número

# Ingrese el primer número: ñ
# Error: debe insertar un valor numérico válido.

#----------------------------------------------------------

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y 
# devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La 
# lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo",
# "Oso"].Usa la función filter()

def filtrar_mascotas_permitidas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))
mascotas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Perro"]
print(filtrar_mascotas_permitidas(mascotas)) # Únicamente devuelve Perro

#----------------------------------------------------------

# 10.  Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el 
# error adecuadamente.

class ListaVaciaError(Exception):
    """Excepción personalizada para cuando la lista está vacía."""
    def __init__(self, mensaje="La lista está vacía, no se puede calcular el promedio."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def calcular_promedio(numeros):
    if len(numeros) == 0:
        raise ListaVaciaError()
    return sum(numeros) / len(numeros)

def probar_promedio(lista):
    try:
        promedio = calcular_promedio(lista)
    except ListaVaciaError as error:
        print(f"Error: {error}")
    else:
        print(f"El promedio es: {promedio}")


probar_promedio([10, 20, 30])   # Devuelve : El promedio es: 20.0
probar_promedio([])             # Devuelve : Error: La lista está vacía, no se puede calcular el promedio.

#----------------------------------------------------------

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa 
# un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 
# o mayor que 120), maneja las excepciones adecuadamente

class EdadInvalidaError(Exception):
    """Excepción personalizada para edades fuera del rango permitido."""
    def __init__(self, mensaje="Estás mintiendo, no es posible que tu edad no esté entre 0 y 120 años."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def pedir_edad():
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad < 0 or edad > 120:
            raise EdadInvalidaError()
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
    except EdadInvalidaError as error:
        print(f"Error: {error}")
    else:
        print(f"Edad registrada correctamente: {edad} años.")
        if 0 <= edad <= 10:
            print(f"¡Qué mono! Tienes {edad} añitos.") # Un añadido que no pide el enunciado, por rizar el rizo

pedir_edad()
# Ingresa tu edad: 121
# Error: Estás mintiendo, no es posible que tu edad no esté entre 0 y 120 años.

# Ingresa tu edad: 2
# Edad registrada correctamente: 2 años.
# ¡Qué mono! Tienes 2 añitos.

#----------------------------------------------------------

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud 
# de cada palabra. Usa la función map()

def longitudes_palabras(frase):
    return list(map(len, frase.split())) # frase.split divide la frase en una lista de palabras, 
                                         # usando los espacios como separador.

frase = "Estoy haciendo Data Analytics"
print(longitudes_palabras(frase)) # Devuelve [5, 8, 4, 9]

#----------------------------------------------------------

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minus(conjunto_letras):
    return list(map(lambda letra: (letra.upper(), letra.lower()), conjunto_letras))
# La función map por cada letra del conjunto, crea una tupla (mayúscula, minúscula).
letras = {'P', 'o', 'w', 'e', 'r'}
resultado = letras_mayus_minus(letras)
print(resultado) # [('P', 'p'), ('E', 'e'), ('O', 'o'), ('W', 'w'), ('R', 'r')]

#----------------------------------------------------------

# 14. Crea una función que retorne las palabras de una lista de 
# palabras que comience con una letra en especifico. Usa la función filter()

def palabras_que_empiezan_con(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))
# palabra.starswith devuelve True si la palabra empieza con esa letra, y False si no.

palabras = ["casa", "perro", "coche", "partido", "camión", "puerro"]
resultado = palabras_que_empiezan_con(palabras, "p")
print(resultado) # Devuelve ['perro', 'partido', 'puerro']

#----------------------------------------------------------

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))
# La lambda exterior recibe la lista completa, mientras que la interior define la función

numeros = [1, 2, 3, 4, 5]
resultado = sumar_tres(numeros)
print(resultado) # Devuelve [4, 5, 6, 7, 8]

#----------------------------------------------------------

# 16. Escribe una función que tome una cadena de texto y un número entero 
# n como parámetros y devuelva una lista de todas las palabras que sean más
# largas que n. Usa la función filter()

def palabras_mas_largas_que(texto, n):
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))
# texto.split divide el texto en una cadena de palabras, separando las palabras por espacios

# filter(lambda palabra: len(palabra) > n, palabras) filtra solo las palabras cuya longitud
# sea mayor que n 

texto = "Estoy haciendo el máster de DataAnalytics en ThePower"
resultado = palabras_mas_largas_que(texto, 5)
print(resultado) # El resultado que devuelve es ['haciendo', 'máster', 'DataAnalytics', 'ThePower']

#----------------------------------------------------------

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def digitos_a_numero(digitos):
    return reduce(lambda acumulador, digito: acumulador * 10 + digito, digitos, 0)
# Reduce no es como map o filter, esta necesita importarse del módulo functools
# Esta va "acumulando" un resultado recorriendo la lista de izquierda a derecha,
# aplicando la función a cada paso entre el acumulador y el siguiente elemento.

# La lógica acumulador * 10 + digito desplaza el número acumulado una posición a la izquierda
# (multiplicando por 10) y le suma el nuevo dígito.
# 1. -> 0 * 10 + 5
# 2. -> 5 * 10 + 7
# 3. -> 57 * 10 + 2
digitos = [5, 7, 2]
resultado = digitos_a_numero(digitos)
print(resultado) # Devuelve 572 como resultado

#----------------------------------------------------------

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga 
# información de estudiantes (nombre, edad, calificación) y use la función filter
# para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 78},
    {"nombre": "Marta", "edad": 21, "calificacion": 90},
    {"nombre": "Carlos", "edad": 23, "calificacion": 85},
    {"nombre": "Sofía", "edad": 19, "calificacion": 92},
]

def estudiantes_sobresalientes(lista_estudiantes):
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_estudiantes))
# la función filter recorre cada diccionario de la lista y se queda solo con aquellos
# donde el valor de la clave "calificacion" sea mayor o igual a 90.

resultado = estudiantes_sobresalientes(estudiantes)
print(resultado) # Devuelve a Ana, a Sofia y a Marta, confirmando que, si el valor es igual a 90 también lo elige

#----------------------------------------------------------

# 19. Crea una función lambda que filtre los números impares de una lista dada

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
# Dentro, filter(lambda x: x % 2 != 0, lista) recorre cada número x y 
# se queda solo con los que cumplen x % 2 != 0 (es decir, los cuales el resto de su división entre 2 es distinto de 0).
lista = [2, 3, 17, 34, 6]

print(filtrar_impares(lista)) # Devuelve 3 y 17 

#----------------------------------------------------------

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()

def filtrar_enteros(lista_mixta):
    return list(filter(lambda elemento: isinstance(elemento, int), lista_mixta))

# isinstance comprueba si un elemento es de tipo int (entero). Devuelve True si lo es, False si no
# la función filter recorre cada elemento de la lista y solo devuelve los que cumplen que isinstance devuelva true

lista_mixta = [1, "leche", 4, "arroz", "pelota"]

print(filtrar_enteros(lista_mixta)) # devuelve 1 y 4

#----------------------------------------------------------

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x ** 3

print(cubo(3)) # devuelve el cubo de 3, 27

print(cubo(cubo(3))) # devuelve el cubo del cubo de 3, 1963

#----------------------------------------------------------

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

def producto_total(lista_numeros):
    return reduce(lambda acumulador, numero: acumulador * numero, lista_numeros)

# reduce() recorre la lista de izquierda a derecha, multiplicando el acumulador por cada nuevo número. 
# reduce() sirve para convertir una lista entera en un solo valor, 
# combinando sus elementos de dos en dos, uno tras otro, hasta que solo queda uno.

numeros = [1, 2, 3, 4]
resultado = producto_total(numeros)
print(resultado) # Devuelve 24

#----------------------------------------------------------

# 23. Concatena una lista de palabras.Usa la función reduce()

from functools import reduce

def concatenar_palabras(lista_palabras):
    return reduce(lambda acumulado, palabra: acumulado + palabra, lista_palabras)

lista_palabras = ("hola", "soy", "Víctor")
print(concatenar_palabras(lista_palabras))

#----------------------------------------------------------

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia_total(lista_numeros):
    return reduce(lambda acumulado, numero: acumulado - numero, lista_numeros)

lista_numeros = (100, 3, 6, 18)
print(diferencia_total(lista_numeros)) # Devuelve 73, resultado de 100-3-6-18

#----------------------------------------------------------

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    return len(texto)
# len cuenta los caracteres de un string 

texto = "Soy Victor"
print(contar_caracteres(texto)) # Devuelve 10 , ya que cuenta el espacio también como caracter

#----------------------------------------------------------

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda a, b: a % b
# % es el operador módulo, que devuelve el resto de una división 

print(resto(10, 5)) # no sobra nada, devuelve 0 

print(resto(10, 3)) # devuelve 1 

#----------------------------------------------------------

# 27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# sum suma los números de la lista y len los cuenta 

numeros = (1, 4, 6, 19)
print(calcular_promedio(numeros)) # devuelve 7.5 

#----------------------------------------------------------

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  # si no hay ningún duplicado
# con vistos creamos un conjunto vacío para ir guardando los elementos que ya hemos visto.
# si recorremos la lista elemento por elemento:
# si el elemento ya está en vistos, significa que es un duplicado → lo devolvemos inmediatamente.
# si no está, lo añadimos a vistos con .add() para recordarlo de cara a los siguientes elementos.

lista = (1, 2, 3, 4, 4, 5, 5, 6) 
print(primer_duplicado(lista)) # devuelve 4, no 4 y 5, ya que buscamos el PRIMER elemento duplicado

#----------------------------------------------------------

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

def enmascarar(valor):
    texto = str(valor) # da igual lo que reciba, lo convierte en string
    if len(texto) <= 4:
        return texto # si el texto es menor o igual a cuatro caracteres lo devuelve tal cual
    return "#" * (len(texto) - 4) + texto[-4:] # si es mayor, enmascara todos los caracteres previos al cuarto último

valor = 2143151351
print(enmascarar(valor)) # Devuelve ######1351 

#----------------------------------------------------------

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden

def son_anagramas(palabra1, palabra2):
    letras1 = sorted(palabra1.replace(" ", "").lower())
    letras2 = sorted(palabra2.replace(" ", "").lower())
    return letras1 == letras2
# replace(): quita los espacios, por si son frases con varias palabras.

# lower(): convierte todo a minúsculas, para que no importe si hay mayúsculas o minúsculas.

# sorted(): ordena alfabéticamente las letras de cada palabra. Si dos palabras son anagramas, 
# al ordenar sus letras deben quedar exactamente iguales.
print(son_anagramas("amor", "roma")) # Devuelve True
print(son_anagramas("amor", "Roma")) # Devuelve True, da igual si es minuscula o mayúscula

#----------------------------------------------------------

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite
# un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje
# indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    # 1. Pedimos la lista de nombres, separados por comas
    entrada = input("Ingresa una lista de nombres separados por comas: ")
    lista_nombres = [nombre.strip() for nombre in entrada.split(",")]

    # 2. Pedimos el nombre a buscar
    nombre_buscado = input("Ingresa el nombre que deseas buscar: ").strip()

    # 3. Buscamos el nombre en la lista
    if nombre_buscado in lista_nombres:
        print(f"✅ El nombre '{nombre_buscado}' fue encontrado en la lista.")
    else:
        # 4. Si no está, lanzamos una excepción
        raise ValueError(f"❌ El nombre '{nombre_buscado}' no se encuentra en la lista.")

buscar_nombre() # Ingresa una lista de nombres separados por comas: pedro, juan, lucia, roberto
                # Ingresa el nombre que deseas buscar: roberto
                # ✅ El nombre 'roberto' fue encontrado en la lista.

#----------------------------------------------------------

# 32. Crea una función que tome un nombre completo y una lista de empleados, 
# busque el nombre completo en la lista y devuelve el puesto del empleado si 
# está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."


# Lista de empleados de ejemplo
empleados = [
    {"nombre": "Ana Gómez", "puesto": "Analista de Datos"},
    {"nombre": "Luis Ramírez", "puesto": "Gerente de Ventas"},
    {"nombre": "Marta Díaz", "puesto": "Desarrolladora"},
]

# Pruebas
print(buscar_puesto("Ana Gómez", empleados))       # Analista de Datos
print(buscar_puesto("Carlos Ruiz", empleados))     # Carlos Ruiz no trabaja aquí.

#----------------------------------------------------------

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# Ejemplo de uso
a = [1, 2, 3]
b = [10, 20, 30]

resultado = sumar_listas(a, b)
print(resultado)  # [11, 22, 33]

#----------------------------------------------------------

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos.
# Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e 
# info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1          # Longitud inicial del tronco
        self.ramas = []          # Lista vacía de ramas

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)    # Cada rama nueva empieza con longitud 1

    def crecer_ramas(self):
        # Aumentamos en 1 la longitud de CADA rama existente
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if posicion < 0 or posicion >= len(self.ramas):
            raise IndexError(f"No existe una rama en la posición {posicion}.")
        self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas,
        }
# Ejemplo de uso : 

arbol = Arbol()

arbol.crecer_tronco()          # tronco: 1 -> 2
arbol.nueva_rama()             # ramas: [1]
arbol.crecer_ramas()           # ramas: [2]
arbol.nueva_rama()             # ramas: [2, 1]
arbol.nueva_rama()             # ramas: [2, 1, 1]
arbol.quitar_rama(2)           # quita el elemento en índice 2 (el último "1") -> ramas: [2, 1]

print(arbol.info_arbol()) # Devuelve : {'longitud_tronco': 2, 'numero_ramas': 2, 'longitudes_ramas': [2, 1]}

#----------------------------------------------------------

# 35. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre,
# saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones 
# como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente  # True o False

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        # Si NO tiene cuenta corriente, no puede quedar en negativo
        if not self.cuenta_corriente and cantidad > self.saldo:
            raise ValueError(
                f"{self.nombre} no tiene saldo suficiente para retirar {cantidad}."
            )
        self.saldo -= cantidad

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        # Se retira de "otro_usuario" y se agrega al usuario actual (self)
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)

    def __str__(self):
        return f"{self.nombre}: saldo = {self.saldo}, cuenta_corriente = {self.cuenta_corriente}"

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)             # Bob: 50 + 20 = 70
alicia.transferir_dinero(bob, 80)  # Bob: 70 - 80 = -10 (permitido, tiene cuenta corriente)
                                    # Alicia: 100 + 80 = 180
alicia.retirar_dinero(50)          # Alicia: 180 - 50 = 130

print(alicia)  # Alicia: saldo = 130, cuenta_corriente = True
print(bob)     # Bob: saldo = -10, cuenta_corriente = True

#----------------------------------------------------------

# 36. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , 
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro 
# de la función procesar_texto.

def contar_palabras(texto):
    # separa el texto en palabras (por espacios) y cuenta cuántas veces aparece cada una
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    # sustituye todas las apariciones de palabra_original por palabra_nueva
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    # separa el texto en palabras, descarta las que coincidan, y vuelve a unir
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        raise ValueError(f"Opción '{opcion}' no reconocida.")

texto = "estoy haciendo el master de restauración en thepower"

# 1. Contar palabras
print(procesar_texto(texto, "contar")) # Devuelve {'estoy': 1, 'haciendo': 1, 'el': 1, 
                                       # 'master': 1, 'de': 1, 'restauración': 1, 'en': 1, 'thepower': 1}

# 2. Reemplazar "restauración" por "DataAnalytics"
print(procesar_texto(texto, "reemplazar", "restauración", "DataAnalytics"))
# Devuelve : estoy haciendo el master de DataAnalytics en thepower

# 3. Eliminar la palabra "de"
print(procesar_texto(texto, "eliminar", "de"))
# Devuelve : estoy haciendo el master restauración en thepower

# 4. Opción inválida (para comprobar el error)
try:
    procesar_texto(texto, "opcion_falsa")
except ValueError as e:
    print(e)
# Opción 'opcion_falsa' no reconocida.

#----------------------------------------------------------

# 37. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento_del_dia():
    hora = int(input("Ingresa la hora (0-23): "))

    if hora < 0 or hora > 23:
        raise ValueError("La hora debe estar entre 0 y 23.")

    if 6 <= hora < 12:
        print("Es de día (mañana).")
    elif 12 <= hora < 20:
        print("Es de tarde.")
    else:  # cubre 20-23 y 0-5
        print("Es de noche.")


determinar_momento_del_dia()
# Devuelve : Ingresa la hora (0-23): 2
# Es de noche.

#----------------------------------------------------------

# 38. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.

def calificacion_en_texto():
    nota = float(input("Ingresa la calificación numérica (0-100): "))

    if nota < 0 or nota > 100:
        raise ValueError("La calificación debe estar entre 0 y 100.")

    if 0 <= nota <= 69:
        resultado = "Insuficiente"
    elif 70 <= nota <= 79:
        resultado = "Bien"
    elif 80 <= nota <= 89:
        resultado = "Muy bien"
    else:  # cubre 90-100
        resultado = "Excelente"

    print(f"Calificación: {resultado}")
    return resultado

calificacion_en_texto()
# Ingresa la calificación numérica (0-100): 80
# Calificación: Muy bien
# 'Muy bien'

#----------------------------------------------------------

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math  # necesitamos math.pi para el círculo

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos          # desempaqueta la tupla (base, altura)
        return base * altura          # área del rectángulo

    elif figura == "circulo":
        radio, = datos                 # desempaqueta tupla de 1 elemento (coma obligatoria)
        return math.pi * radio ** 2    # área del círculo

    elif figura == "triangulo":
        base, altura = datos          # desempaqueta la tupla (base, altura)
        return (base * altura) / 2    # área del triángulo

    else:
        raise ValueError(f"Figura '{figura}' no reconocida.")  # figura no válida


# Demostración 

print(calcular_area("rectangulo", (4, 5)))    # Devuelve : 20
print(calcular_area("circulo", (3,)))         # Devuelve : 28.27433...
print(calcular_area("triangulo", (6, 4)))     # Devuelve : 12.0
print(calcular_area("romboide", (4, 5)))      # Devuelve : ValueError: Figura 'romboide' no reconocida.

#----------------------------------------------------------

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento.

def calcular_compra():
    precio_original = float(input("Ingresa el precio original del artículo: "))  # pide el precio

    tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): ").strip().lower()
    # .strip() quita espacios, .lower() pasa todo a minúsculas (para aceptar "Si", "SI", etc.)

    if tiene_cupon == "si":
        valor_cupon = float(input("Ingresa el valor del cupón de descuento: "))  # pide el cupón

        if valor_cupon > 0:                    # solo si el cupón es válido (mayor a 0)
            precio_final = precio_original - valor_cupon   # resta el descuento
            if precio_final < 0:               # evita que el precio final sea negativo
                precio_final = 0
            print(f"Precio final con descuento aplicado: {precio_final}€")
        else:
            # el cupón es 0 o negativo -> no se aplica
            print(f"Cupón no válido. Precio final: {precio_original}€")

    elif tiene_cupon == "no":
        print(f"Precio final sin descuento: {precio_original}€")   # no hay descuento

    else:
        # el usuario no respondió "si" ni "no"
        raise ValueError("Respuesta no válida, debes responder 'si' o 'no'.")


calcular_compra()

# Ingresa el precio original del artículo: 40
# ¿Tienes un cupón de descuento? (si/no): si
# Ingresa el valor del cupón de descuento: 10
# Precio final con descuento aplicado: 30.0€