from Matriz import Matriz
from Ordenamiento import Ordenamiento


def mostrar_matriz(matriz):

    for fila in matriz:
        print(fila)


def pedir_matriz(filas, columnas):

    matriz = []

    for i in range(filas):

        fila = []

        for j in range(columnas):
            numero = float(input("Digite el numero: "))
            fila.append(numero)

        matriz.append(fila)

    return matriz


continuar = True

while continuar:

    print("\n==============================")
    print("       MENU PRINCIPAL")
    print("==============================")
    print("1. Punto 3.1 - Matrices")
    print("2. Punto 3.2 - Ordenamientos")
    print("3. Salir")

    opcion = int(input("Digite una opcion: "))

    if opcion == 1:

        print("\n===== PUNTO 3.1 =====")
        print("OPERACIONES CON MATRICES")

        filas1 = int(input("Filas de la matriz 1: "))
        columnas1 = int(input("Columnas de la matriz 1: "))

        print("\nDigite la matriz 1:")
        matriz1 = pedir_matriz(filas1, columnas1)

        filas2 = int(input("\nFilas de la matriz 2: "))
        columnas2 = int(input("Columnas de la matriz 2: "))

        print("\nDigite la matriz 2:")
        matriz2 = pedir_matriz(filas2, columnas2)

        vector = []

        print("\nDigite los valores del vector:")

        for i in range(columnas1):
            numero = float(input("Digite el numero: "))
            vector.append(numero)

        objeto = Matriz(matriz1, matriz2, vector)

        volver = False

        while not volver:

            print("\n------ SUBMENU 3.1 ------")
            print("1. Suma de matrices")
            print("2. Producto de matrices")
            print("3. Inversa de matriz")
            print("4. Producto de matriz por vector")
            print("5. Regresar al menu principal")

            opcion2 = int(input("Digite una opcion: "))

            if opcion2 == 1:

                if filas1 == filas2 and columnas1 == columnas2:

                    objeto.sumar()

                    resultado = objeto.get()

                    print("\nResultado de la suma:")
                    mostrar_matriz(resultado)

                else:
                    print("\nLas matrices deben tener el mismo tamaño.")

            elif opcion2 == 2:

                if columnas1 == filas2:

                    objeto.multiplicar()

                    resultado = objeto.get()

                    print("\nResultado del producto:")
                    mostrar_matriz(resultado)

                else:
                    print("\nNo se pueden multiplicar estas matrices.")

            elif opcion2 == 3:

                if filas1 == columnas1:

                    objeto.inversa()

                    resultado = objeto.get()

                    if resultado == []:
                        print("\nLa matriz no tiene inversa.")
                    else:
                        print("\nMatriz inversa:")
                        mostrar_matriz(resultado)

                else:
                    print("\nLa matriz debe ser cuadrada.")

            elif opcion2 == 4:

                if columnas1 == len(vector):

                    objeto.matriz_vector()

                    resultado = objeto.get()

                    print("\nResultado de matriz por vector:")

                    for numero in resultado:
                        print(numero)

                else:
                    print("\nEl vector no tiene el tamaño correcto.")

            elif opcion2 == 5:

                volver = True

            else:
                print("\nOpcion incorrecta.")

    elif opcion == 2:

        print("\n===== PUNTO 3.2 =====")
        print("ORDENAMIENTO DE NUMEROS FLOTANTES")

        cantidad = int(input("Cuantos numeros desea ingresar: "))

        lista = []

        for i in range(cantidad):

            numero = float(input("Digite un numero: "))

            lista.append(numero)

        objeto = Ordenamiento(lista)

        volver = False

        while not volver:

            print("\n------ SUBMENU 3.2 ------")
            print("1. Burbuja")
            print("2. Insercion")
            print("3. Seleccion")
            print("4. Mergesort")
            print("5. Sort de Python")
            print("6. Regresar al menu principal")

            opcion2 = int(input("Digite una opcion: "))

            if opcion2 == 1:

                objeto.burbuja()

                resultado = objeto.get()

                print("\nResultado:")
                print(resultado)

            elif opcion2 == 2:

                objeto.insercion()

                resultado = objeto.get()

                print("\nResultado:")
                print(resultado)

            elif opcion2 == 3:

                objeto.seleccion()

                resultado = objeto.get()

                print("\nResultado:")
                print(resultado)

            elif opcion2 == 4:

                objeto.mergesort()

                resultado = objeto.get()

                print("\nResultado:")
                print(resultado)

            elif opcion2 == 5:

                objeto.sort_python()

                resultado = objeto.get()

                print("\nResultado:")
                print(resultado)

            elif opcion2 == 6:

                volver = True

            else:
                print("\nOpcion incorrecta.")

    elif opcion == 3:

        continuar = False

    else:

        print("\nOpcion incorrecta.")


print("\nPrograma terminado.")