import sys

if len(sys.argv) == 4:
    print(f"El primer parametro ingresado es {sys.argv[1]}")
    print(type(sys.argv[1]))
    print(f"El primer parametro ingresado es {sys.argv[2]}")
    print(f"El primer parametro ingresado es {sys.argv[3]}")

else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py 1 2 3')

