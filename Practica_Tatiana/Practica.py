'''
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
import random
import math

class Punto1_Vector_de_double ():

#--------------------------------------Crear Vector de double----------------------------------------------------------#
    vector_doubles = []

#--------------------------------------------Rellenar vector de double-------------------------------------------------#
    def rellenar_vector_doubles(self, largo):
        for linea in range(largo):
            self.vector_doubles.append(random.uniform(0.0, 100.0))


#-----------------------------------------Recorrer calcular las raices-------------------------------------------------#
    def recorrer_vector_de_doubles_calculo_raices(self):
        cadena_de_resultados = ''
        for linea in range(len(self.vector_doubles)):
            resultado_de_raiz = math.sqrt(self.vector_doubles[linea])
            cadena_de_resultados += str(resultado_de_raiz) + ' '
        return cadena_de_resultados

#----------------------------------Resta un numero a todas las posiciones----------------------------------------------#
    def recorrer_vector_de_doubles_restar_un_numero(self, numero):
        cadena_de_resultados = ''
        for linea in range(len(self.vector_doubles)):
            resultado_de_la_resta = self.vector_doubles[linea] - numero
            cadena_de_resultados += str(resultado_de_la_resta) + ' '
        return cadena_de_resultados

#------------------------------------------Imprimir vector de doubles--------------------------------------------------#
    def impresion_de_vector_double(self):
        cadena_de_texto = ''
        for linea in range(len(self.vector_doubles)):
            cadena_de_texto += str(self.vector_doubles[linea]) + ' '
        return cadena_de_texto


#------------------------------------------------Llamado de metodos anteriores-----------------------------------------#
    def vector_double(self):
        self.rellenar_vector_doubles(10)
        print(self.recorrer_vector_de_doubles_calculo_raices())
        print(self.recorrer_vector_de_doubles_restar_un_numero(-5))
        print(self.impresion_de_vector_double())

class Punto2_vector_de_enteros():
#--------------------------------------Crear Vector de enteros---------------------------------------------------------#
    vector_enteros = []

#----------------------------------Rellenar vector de enteros----------------------------------------------------------#
    def rellenar_vector_de_enteros(self, largo):
            for linea in range(largo):
                self.vector_enteros.append(random.randint(0, 100))

#-----------------------------------Impirmir el vector de enteros------------------------------------------------------#
    def impresion_de_vector_enteros(self):
        cadena_de_enteros = ''
        for linea in range(len(self.vector_enteros)):
            cadena_de_enteros += str(self.vector_enteros[linea]) + ' '
        return cadena_de_enteros

#-------------------------------Recorrer y obtener los numeros de un rango---------------------------------------------#
    def recorrer_vector_de_enteros_obtener_numeros_rango(self, numero1, numero2):
        cadena_de_resultados = ''
        for linea in range(len(self.vector_enteros)):
           valor_de_casilla_actual = self.vector_enteros[linea]
           if valor_de_casilla_actual>numero1 and valor_de_casilla_actual<numero2:
            cadena_de_resultados += str(valor_de_casilla_actual)+ ' '
        return cadena_de_resultados
#------------------------------------------------Llamado de metodos anteriores-----------------------------------------#
    def vector_numeros_aleatoreos(self):
        self.rellenar_vector_de_enteros(10)
        print (self.recorrer_vector_de_enteros_obtener_numeros_rango(0,20))
        # Numeros primos
        # pares e impares => return indice y el numero
        #invertir arreglo
        #obtener largo
        #obtener elemento del medio
        print(self.impresion_de_vector_enteros())

#Eliminar elemento ejercicio #3
a = Punto1_Vector_de_double()
a.vector_double()
b = Punto2_vector_de_enteros()
b.vector_numeros_aleatoreos()
