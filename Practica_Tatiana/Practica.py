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
        print('-------------------------Calculos de raices-------------------------------------')
        print(self.recorrer_vector_de_doubles_calculo_raices()+'\n')
        print('-------------------------Restar un numero---------------------------------------')
        print(self.recorrer_vector_de_doubles_restar_un_numero(-5)+'\n')
        print('-------------------------Vector completo----------------------------------------')
        print(self.impresion_de_vector_double()+'\n')

class Punto2_vector_de_enteros():
#--------------------------------------Crear Vector de enteros---------------------------------------------------------#
    vector_enteros = []

#----------------------------------Rellenar vector de enteros----------------------------------------------------------#
    def rellenar_vector_de_enteros(self, largo):
            for linea in range(largo):
                self.vector_enteros.append(random.randint(0, 100))


#-------------------------------Recorrer y obtener los numeros de un rango---------------------------------------------#
    def recorrer_vector_de_enteros_obtener_numeros_rango(self, numero1, numero2):
        cadena_de_resultados = ''
        for linea in range(len(self.vector_enteros)):
           valor_de_casilla_actual = self.vector_enteros[linea]
           if valor_de_casilla_actual>numero1 and valor_de_casilla_actual<numero2:
            cadena_de_resultados += str(valor_de_casilla_actual)+ ' '
        return cadena_de_resultados

#-------------------------------Recorrer y obtener los numeros primos y sus indices------------------------------------#
    def recorrer_vector_de_enteros_obtener_numeros_primos(self):
        cadena_de_resultados = ''
        indice_divisor= 0
        for linea in range(len(self.vector_enteros)):
            valor_de_casilla_actual = self.vector_enteros[linea]
            divisor= 0
            primo = True
            if valor_de_casilla_actual is 2:
                primo = True

            elif valor_de_casilla_actual % 2 is 0:
                primo = False
                divisor = 2
            else:
                mediaRelativa = int((valor_de_casilla_actual - 1) / 2)
                for contador in range(3, mediaRelativa):
                    if valor_de_casilla_actual % contador is 0:
                        primo = False
                        divisor = contador
                        break
            cadena_de_resultados += 'Numero: '+ str(valor_de_casilla_actual)+' Primo: '+ str(primo)+ ' Indice: '+str(divisor)+ '  '
        return cadena_de_resultados

#------------------------------------Recorrer y obtener pares e impares------------------------------------------------#
    def recorrer_vector_de_enteros_numeros_pares(self):
        cadena_de_resultados = ''
        for linea in range(len(self.vector_enteros)):
            valor_de_casilla_actual = self.vector_enteros[linea]
            if valor_de_casilla_actual %2 is 0:
                cadena_de_resultados += 'Par: '+str(valor_de_casilla_actual)+ ' '
            else:
                cadena_de_resultados += 'Impar: ' + str(valor_de_casilla_actual) + ' '
        return cadena_de_resultados

#------------------------------------Recorrer e invertir el orden------------------------------------------------------#
    def recorrer_vector_de_enteros_invertir_orden(self):
        cadena_de_resultados = ''
        inversor = len(self.vector_enteros)-1
        for linea in range(len(self.vector_enteros)):
            valor_de_casilla_actual = self.vector_enteros[inversor]
            cadena_de_resultados += str(valor_de_casilla_actual)+ ' '
            inversor -= 1
        return cadena_de_resultados

#-----------------------------------Recorrer y obtener valor del medio--------------------------------------------------#
    def recorre_vector_de_enteros_valor_del_medio(self):
        cadena_de_enteros = ''
        largo_de_vector = int(len(self.vector_enteros))
        if largo_de_vector % 2  is 0:
            largo_de_vector = int(largo_de_vector/2)
            cadena_de_enteros += str(self.vector_enteros[largo_de_vector - 1]) + ' '
            cadena_de_enteros += str(self.vector_enteros[largo_de_vector])
        else:
            largo_de_vector = int(((largo_de_vector-1)/2))
            cadena_de_enteros += str(self.vector_enteros[largo_de_vector]) + ' '

        return cadena_de_enteros

#-----------------------------------------Impresion de Vector----------------------------------------------------------#
    def impresion_de_vector_enteros(self):
        cadena_de_resultados = ''
        for linea in range(len(self.vector_enteros)):
            cadena_de_resultados += str(self.vector_enteros[linea])+ ' '
        return cadena_de_resultados

#------------------------------------------------Llamado de metodos anteriores-----------------------------------------#
    def vector_numeros_aleatoreos(self):
        self.rellenar_vector_de_enteros(9)
        print('-------------------------Numeros del rango--------------------------------------')
        print (self.recorrer_vector_de_enteros_obtener_numeros_rango(0,20)+'\n')
        print('--------------------------Numeros primos----------------------------------------')
        print(self.recorrer_vector_de_enteros_obtener_numeros_primos()+'\n')
        print('--------------------------Numeros pares e impares-------------------------------')
        print(self.recorrer_vector_de_enteros_numeros_pares() + '\n')
        print('-------------------------Invertir el orden--------------------------------------')
        print(self.recorrer_vector_de_enteros_invertir_orden()+'\n')
        #obtener largo
        print('-------------------------Valor del medio----------------------------------------')
        print(self.recorre_vector_de_enteros_valor_del_medio()+'\n')
        print('-------------------------Vector completo----------------------------------------')
        print(self.impresion_de_vector_enteros())
        print('-------------------------Imprimir sin el primero--------------------------------')
        self.eliminar_primero()
        print(self.impresion_de_vector_enteros())

    def eliminar_primero(self):

        self.vector_enteros[0] =''
        return  self.vector_enteros

a = Punto1_Vector_de_double()
a.vector_double()
b = Punto2_vector_de_enteros()
b.vector_numeros_aleatoreos()
