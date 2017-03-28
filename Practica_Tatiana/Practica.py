'''
1. Crear  y alimentar un vector, 1000 elementos tipo double.
    a. Crear un método que calcule las raíces cuadradas de cada entrada del arreglo
    b. Crear un método que reste n unidades a cada entrada del arreglo
2. Crear y alimentar un vector de números enteros generados aleatoriamente.
    a. Obtener un rango de elementos de dicho vector, donde el rango está dado por el índice a y b tomando en cuenta que rango no debe superar las dimensiones del arreglo.
    b. Obtener los números primos que se encuentra en el arreglo
    c. Obtener los números pares e impares
            i. Se devuelve el índice
            ii. Se devuelve el numero
    d. Invertir arreglo
            i. Se invierte el orden del arreglo, esto es si se tiene el arreglo: [a,b,c,d,r,f,g,] la salida de invertir seria: [g,f,r,d,c,d,a]
    e. Obtener el Largo de un Arreglo:
            i. [g,f,r,d,c,d,a] -> 6
            ii. [] -> 0
    f. Obtener el elemento medio de un arreglo
            i. Devuelve la posición largo/2 del arreglo en caso de no ser división entera devuelve la posición largo-1/2
3. Eliminar el primer elemento un vector:
       Entrada: [a,b,n,m,x,]
       Salida: [b,n,m,x,]
'''


class ejercicios ():
    matriz = []
    #def __init__(self, matriz):
     #self.matriz = matriz

    def rellenar_matriz(self, largo):
        for linea in range(largo):
            self.matriz.append([])
            for columna in range(largo):
                self.matriz[linea].append("Hola")

    def matriz_double(self, matriz):
        self.rellenar_matriz(1000)
        # Rellenar matriz
        # Recorrer matriz
        # restar n numero de matriz

    def matriz_numeros_aleatoreos(self):
        print("hola")
        #Rellenar matriz
        #Rango de a-b -busque nuemeros
        #Numeros primos
        #pares e impares => return indice y el numero
        #Invertir arreglo
        #largo del arreglo

    def eliminar_elemento(self):
        print("hola")
        #Eliminar elemento inicial

    def impresion_matriz(self):
        cadena_de_sring = ''
        for linea in range(len(self.matriz)):
            for columna in range(len(self.matriz[linea])):
                cadena_de_sring += str(self.matriz[linea][columna]) + ' '
            cadena_de_sring += '\n'
        return cadena_de_sring


a = ejercicios()
a.impresion_matriz()
a.matriz_double(a.matriz)
a.impresion_matriz()