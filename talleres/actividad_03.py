# Alejandro Vergara Tamayo 2456556

import math

#Entrada ==>
# 'diametroCirculo' es la entrada la cual el usuario inserta (float)

def areaCirculo (diametroCirculo:float) -> float: # 'diametroCirculo: float' tipado de variable
    radio = diametroCirculo / 2
    area = round(math.pi*(pow(radio,2)),2) # Redondeamos a 2 unidades decimales
    return area

print(areaCirculo(42))
print(areaCirculo(10))
print(areaCirculo(20))