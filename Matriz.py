class Matriz:

    def __init__(self, matriz1, matriz2, vector):
        self.matriz1 = matriz1
        self.matriz2 = matriz2
        self.vector = vector
        self.resultado = []

    def sumar(self):
        filas = len(self.matriz1)
        columnas = len(self.matriz1[0])

        self.resultado = []

        for i in range(filas):
            fila = []

            for j in range(columnas):
                fila.append(self.matriz1[i][j] + self.matriz2[i][j])

            self.resultado.append(fila)

    def multiplicar(self):
        filas = len(self.matriz1)
        columnas = len(self.matriz2[0])

        self.resultado = []

        for i in range(filas):
            fila = []

            for j in range(columnas):
                suma = 0

                for k in range(len(self.matriz2)):
                    suma = suma + self.matriz1[i][k] * self.matriz2[k][j]

                fila.append(suma)

            self.resultado.append(fila)

    def matriz_vector(self):
        self.resultado = []

        for i in range(len(self.matriz1)):
            suma = 0

            for j in range(len(self.vector)):
                suma = suma + self.matriz1[i][j] * self.vector[j]

            self.resultado.append(suma)

    def inversa(self):
        n = len(self.matriz1)

        matriz = []

        for i in range(n):
            fila = []

            for j in range(n):
                fila.append(float(self.matriz1[i][j]))

            for j in range(n):
                if i == j:
                    fila.append(1.0)
                else:
                    fila.append(0.0)

            matriz.append(fila)

        for i in range(n):

            if matriz[i][i] == 0:

                for k in range(i + 1, n):

                    if matriz[k][i] != 0:
                        matriz[i], matriz[k] = matriz[k], matriz[i]
                        break

            pivote = matriz[i][i]

            if pivote == 0:
                self.resultado = []
                return

            for j in range(2 * n):
                matriz[i][j] = matriz[i][j] / pivote

            for k in range(n):

                if k != i:
                    factor = matriz[k][i]

                    for j in range(2 * n):
                        matriz[k][j] = matriz[k][j] - factor * matriz[i][j]

        self.resultado = []

        for i in range(n):
            fila = []

            for j in range(n, 2 * n):
                fila.append(matriz[i][j])

            self.resultado.append(fila)

    def get(self):
        return self.resultado