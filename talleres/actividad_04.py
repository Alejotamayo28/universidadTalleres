# Alejandro Vergara Tamayo 2456556

#ENTRADAS ==> 
# 'capacidad_maxima' (entrada del usuario para conocer la capacidad maxima con la bateria cargada) => float
# 'maxima_cantidad_recorrida' (entrada del usuario para conocer cuanto fue la cantidad recorrida en la patineta) => float

def energiaConsumida (capacidad_maxima_almacenamiento: float, maxima_cantidad_recorrida: float) -> float:
    consumo_recorrido_por_kilometro = maxima_cantidad_recorrida / capacidad_maxima_almacenamiento
    return (round(consumo_recorrido_por_kilometro,4))

print(energiaConsumida(41,30)) #Caso prueba del taller ==> Salida energia que consume el vehiculo por kilometro recorrido)
print(energiaConsumida(30,10))
print(energiaConsumida(100,210))