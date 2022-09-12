
from ast import If


def tabla (contador, opcion):
    print(contador * opcion)
LIMITE = 11

menu = """
Bienvenido, ¿que tabla deseas conocer?

1 - Tabla del 1
2 - Tabla del 2
3 - Tabla del 3
4 - Tabla del 4
5 - Tabla del 5
6 - Tabla del 6
7 - Tabla del 7
8 - Tabla del 8
9 - Tabla del 9
10 - Tabla del 10

Elige una opción: """

opcion = int(input (menu))

if int(opcion) < LIMITE:
    for i in range (1,11):
        print(str(opcion) + " * " + str(i) + " = " + str(opcion*i))

else:
    print("ingrese un número correcto por favor")
