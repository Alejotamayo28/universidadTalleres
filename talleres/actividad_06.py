# Alejandro Vergara Tamayo 2456556

#Entradas 
# 'kilos_azucas' es la entrada que el usuario ingresa para conocer cuantas bananas se pueden producir con esta cantidad
# tipo (float)


#Costantes
# 'peso_promedio', constante que nos brinda la empresa que fabrica las bananas
# 'desperdicio' , constante que nos brinda la empresa que fabrica las bananas

def fabricaDulces (kilos_azucar: float) -> int:
    peso_promedio = 50
    desperdicio = 10/100
    kilos_azucar *= 1000
    desperdicio_gramos_azucar = kilos_azucar * desperdicio
    kilos_azucar -= desperdicio_gramos_azucar
    total_bananas = round(kilos_azucar / peso_promedio)
    print(total_bananas)


fabricaDulces(6)
fabricaDulces(10)
fabricaDulces(2.2)