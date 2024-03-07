# Alejandro Vergara Tamayo 2456556

import math

def velocidadFinal (velocidadInicial,aceleracion,tiempo) :
 velocidad_final =  (velocidadInicial) + (aceleracion*tiempo)
 return velocidad_final
print("PRIMER EJERCICIO")
print(velocidadFinal(10,2,8)) # CASO_PRUEBA_DEL_TALLER
print(velocidadFinal(0,9.8,5)) # CASO_PRUEBA_DEL_TALLER


def determinarAltura(velocidadInicial, aceleracion, tiempo) :
 altura =  (velocidadInicial*tiempo)+((1/2)*(aceleracion*(pow(tiempo,2))))
 return altura
print("SEGUNDO EJERCICIO")
print(determinarAltura(10,2,8)) # CASO_PRUEBA_DEL_TALLER
print(round(determinarAltura(0,9.8,5),1)) # CASO_PRUEBA_DEL_TALLER ==> Redondeamos a una unidad


def tercerEjercicio(G,M,R,h): 
 g = ((G*M)/pow((R+h),2))
 return g
print("TERCER EJERCICIO")
print(tercerEjercicio(10,8,4,6)) # CASO_PRUEBA_DEL_TALLER

