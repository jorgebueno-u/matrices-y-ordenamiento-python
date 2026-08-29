class Ordenamiento:

    def __init__(self, lista):
        self.lista = lista
        self.resultado = []

    def burbuja(self):

        lista = self.lista.copy()

        for i in range(len(lista)):

            for j in range(len(lista) - i - 1):

                if lista[j] > lista[j + 1]:
                    temporal = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temporal

        self.resultado = lista

    def insercion(self):

        lista = self.lista.copy()

        for i in range(1, len(lista)):

            valor = lista[i]
            j = i - 1

            while j >= 0 and lista[j] > valor:
                lista[j + 1] = lista[j]
                j = j - 1

            lista[j + 1] = valor

        self.resultado = lista

    def seleccion(self):

        lista = self.lista.copy()

        for i in range(len(lista)):

            menor = i

            for j in range(i + 1, len(lista)):

                if lista[j] < lista[menor]:
                    menor = j

            temporal = lista[i]
            lista[i] = lista[menor]
            lista[menor] = temporal

        self.resultado = lista

    def mergesort_lista(self, lista):

        if len(lista) <= 1:
            return lista

        mitad = len(lista) // 2

        izquierda = self.mergesort_lista(lista[:mitad])
        derecha = self.mergesort_lista(lista[mitad:])

        resultado = []

        i = 0
        j = 0

        while i < len(izquierda) and j < len(derecha):

            if izquierda[i] < derecha[j]:
                resultado.append(izquierda[i])
                i = i + 1
            else:
                resultado.append(derecha[j])
                j = j + 1

        while i < len(izquierda):
            resultado.append(izquierda[i])
            i = i + 1

        while j < len(derecha):
            resultado.append(derecha[j])
            j = j + 1

        return resultado

    def mergesort(self):

        self.resultado = self.mergesort_lista(self.lista.copy())

    def sort_python(self):

        lista = self.lista.copy()
        lista.sort()

        self.resultado = lista

    def get(self):
        return self.resultado