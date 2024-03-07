# Alejandro Vergara Tamayo 2456556

#Entradas ==>
# 'monto_total_compra' es el total a pagar de los articulos que el usuario escogio (entero) 

#Constantes ==> 
# 'descuento' constante de descuento que la tienda ofrece (entero)

def descuentoPrendaPagar (monto_total_compra: int) -> int:
    descuento: int = 30
    precio_pagar = round(monto_total_compra - (monto_total_compra * (descuento/100)))
    print(precio_pagar)

descuentoPrendaPagar(119000) #Caso prueba del taller ==> Salida monto a pagar despues del descuento
descuentoPrendaPagar(9000)
descuentoPrendaPagar(1000)