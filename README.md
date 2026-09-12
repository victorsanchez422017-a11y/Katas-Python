# Katas de Python.

## Descripcion del Proyecto

Este repositorio recoge la resolucion de 41 katas (ejercicios practicos) de Python, desarrollados como parte del master de Data Analytics en The Power. El objetivo es reforzar los fundamentos del lenguaje: estructuras de datos, programacion funcional, manejo de excepciones, recursividad y programacion orientada a objetos.

Cada ejercicio se resuelve de forma independiente y va encabezado por un comentario con el enunciado original, junto con ejemplos de uso y el resultado esperado impreso en consola.

## Estructura del Proyecto

```
├── Katas\_python.py   # Ejercicios resueltos (41 katas)
└── README.md         # Descripcion del proyecto
```

## Requisitos

Unicamente se utilizan modulos de la biblioteca estandar: `functools` (para `reduce`) y `math` (para calculos con pi). No se requieren dependencias externas.

Algunos ejercicios (edad, precio, hora, busqueda de nombres) leen datos por teclado con `input()`, por lo que ejecutar el script completo requiere introducir varios valores en consola de forma secuencial.

## Contenido y Detalle de los Ejercicios

### 1\. Cadenas y colecciones (katas 1, 12, 13, 14, 16, 23, 25, 27, 28, 29, 30)

* Kata 1 (`contar\_letras`): construye un diccionario de frecuencias recorriendo la cadena en minusculas e ignorando los espacios.
* Kata 12 (`longitudes\_palabras`): aplica `map(len, ...)` sobre la lista de palabras obtenida con `split()`.
* Kata 13 (`letras\_mayus\_minus`): usa `map()` con `lambda` sobre un conjunto (`set`) para generar tuplas (mayuscula, minuscula) sin letras repetidas.
* Kata 14 (`palabras\_que\_empiezan\_con`): usa `filter()` junto con `str.startswith()`.
* Kata 16 (`palabras\_mas\_largas\_que`): filtra palabras por longitud con `filter()`.
* Kata 23 (`concatenar\_palabras`): usa `reduce()` para ir concatenando los elementos de una lista.
* Kata 25 (`contar\_caracteres`): cuenta caracteres con `len()`, incluyendo espacios.
* Kata 27 (`calcular\_promedio`): calcula la media de una lista con `sum()` y `len()`, sin control de lista vacia.
* Kata 28 (`primer\_duplicado`): recorre la lista apoyandose en un conjunto (`set`) para detectar el primer elemento repetido.
* Kata 29 (`enmascarar`): convierte el valor a texto y sustituye todos los caracteres salvo los ultimos cuatro por `#`.
* Kata 30 (`son\_anagramas`): normaliza las cadenas (minusculas, sin espacios) y compara las letras ordenadas con `sorted()`.

### 2\. Programacion funcional: map, filter, reduce (katas 2, 4, 7, 9, 17, 18, 20, 22, 24, 33)

* Kata 2 (`dobles`): `map()` con `lambda` para duplicar cada valor de la lista.
* Kata 4 (`calcular\_diferencia`): `map()` con `lambda` de dos argumentos aplicada sobre dos listas en paralelo.
* Kata 7 (`tuplas\_a\_strings`): `map(str, ...)` para convertir tuplas a su representacion en texto.
* Kata 9 (`filtrar\_mascotas\_permitidas`): `filter()` para excluir especies prohibidas de una lista.
* Kata 17 (`digitos\_a\_numero`): `reduce()` que reconstruye un numero acumulando digito a digito (`acumulador \* 10 + digito`).
* Kata 18 (`estudiantes\_sobresalientes`): `filter()` sobre una lista de diccionarios segun la clave `calificacion`.
* Kata 20 (`filtrar\_enteros`): `filter()` con `isinstance()` para separar tipos en una lista mixta.
* Kata 22 (`producto\_total`): `reduce()` para el producto acumulado de una lista.
* Kata 24 (`diferencia\_total`): `reduce()` para la resta acumulada de una lista.
* Kata 33 (`sumar\_listas`): `map()` con `lambda` de dos argumentos, encapsulada en una `lambda` exterior.

### 3\. Funciones lambda de una linea (katas 15, 19, 21, 26)

* Kata 15 (`sumar\_tres`): suma 3 a cada elemento de una lista.
* Kata 19 (`filtrar\_impares`): combina `lambda` y `filter()` para quedarse con los numeros impares.
* Kata 21 (`cubo`): calcula el cubo de un numero.
* Kata 26 (`resto`): calcula el resto de una division con el operador `%`.

### 4\. Manejo de excepciones (katas 8, 10, 11, 31, 41)

* Kata 8 (`dividir\_numeros`): `try/except/else` para capturar `ValueError` (entrada no numerica) y `ZeroDivisionError`.
* Kata 10 (`calcular\_promedio` y `ListaVaciaError`): excepcion personalizada, heredada de `Exception`, con mensaje por defecto, lanzada cuando la lista esta vacia.
* Kata 11 (`pedir\_edad` y `EdadInvalidaError`): valida que la edad introducida este entre 0 y 120, combinando una excepcion propia con `ValueError` para entradas no numericas.
* Kata 31 (`buscar\_nombre`): lanza `ValueError` si el nombre buscado no esta en la lista introducida por el usuario.
* Kata 41 (`calcular\_compra`): valida la respuesta del usuario (si/no) y el valor del cupon, lanzando `ValueError` ante respuestas no reconocidas.

### 5\. Recursividad (kata 6)

* Kata 6 (`factorial`): implementacion recursiva con caso base en 0 y 1, y validacion de valores negativos mediante `ValueError`.

### 6\. Programacion orientada a objetos (katas 34, 35)

* Kata 34 (clase `Arbol`): atributos `tronco` y `ramas`; metodos `crecer\_tronco`, `nueva\_rama`, `crecer\_ramas`, `quitar\_rama` e `info\_arbol`.
* Kata 35 (clase `UsuarioBanco`): atributos `nombre`, `saldo` y `cuenta\_corriente`; metodos `retirar\_dinero`, `agregar\_dinero` y `transferir\_dinero`, con logica distinta segun si el usuario dispone o no de cuenta corriente (puede o no quedar en saldo negativo).

### 7\. Condicionales y flujo de control (katas 3, 5, 32, 36, 37, 38, 40)

* Kata 3 (`filtrar\_palabras`): list comprehension que filtra palabras que contienen una palabra objetivo.
* Kata 5 (`evaluar\_notas`): calcula la media de una lista de notas y la compara con un umbral configurable (`nota\_aprobado`).
* Kata 32 (`buscar\_puesto`): recorre una lista de diccionarios de empleados y devuelve el puesto o un mensaje si la persona no esta.
* Kata 36 (`procesar\_texto`): combina tres subfunciones (`contar\_palabras`, `reemplazar\_palabras`, `eliminar\_palabra`) seleccionadas mediante un parametro `opcion`.
* Kata 37 (`determinar\_momento\_del\_dia`): clasifica una hora (0-23) en manana, tarde o noche.
* Kata 38 (`calificacion\_en\_texto`): convierte una nota numerica (0-100) en una calificacion textual (Insuficiente, Bien, Muy bien, Excelente).
* Kata 40 (`calcular\_area`): calcula el area de un rectangulo, circulo o triangulo segun la figura y los datos recibidos, usando `math.pi` para el circulo.

> La numeracion de los ejercicios salta del 38 al 40; la kata 39 no esta presente en el archivo de enunciados.

## Autor

* Víctor Sánchez Toledo

