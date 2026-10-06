'''
Instrucciones: Diseñar un pequeño programa que solicite tres datos al usuario, 
los almacene en variables y posteriormente los muestre en pantalla.

# 1. Entrada de datos: solicitamos la información al usuario y la guardamos en variables
Pais_destino= input("Ingresa el Pais de destino: ")
Cantidad_de_dias= int(input("Ingresa la cantidad de dias: "))
Cantidad_de_personas=int(input("Ingresa la cantidad de personas: "))

print()  # Imprime un salto de línea para separar la entrada del resultado

# 2. Salida de datos: mostramos en pantalla la información almacenada
print("Pais destino:", Pais_destino)
print("Cantidad de dias:", Cantidad_de_dias)
print("Cantidad de personas:", Cantidad_de_personas)
'''
# =========================================================
# Cálculo de descuento para adulto mayor
# =========================================================

# CONSTANTES DEL CÓDIGO (UPPER_SNAKE_CASE)
DESCUENTO_ADULTO_MAYOR = 0.15  # Equivalente al 15%

# Entrada simulada (o captura con input)
subtotal = float(input("Ingresa el precio: "))


# Cálculo del descuento
monto_descuento = subtotal * DESCUENTO_ADULTO_MAYOR
total_pagar = subtotal - monto_descuento

# Salida de datos formateada
print(f"El porcentaje de descuento es: {int(DESCUENTO_ADULTO_MAYOR * 100)}%")
print(f"El descuento aplicado es de:   CRC {monto_descuento:.2f}")
print(f"El total a pagar es de:        CRC {total_pagar:.2f}")