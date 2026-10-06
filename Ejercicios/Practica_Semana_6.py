""" compra = float( input( "Monto de la compra: "))
descuento = 0
if compra > 30000:
  descuento = compra * 0.05
  
elif compra > 60000:
  descuento = compra * 0.10

elif compra > 100000:
   descuento = compra * 0.15
total = compra - descuento
print( "Descuento:", descuento)
print( "Total:", total)
"""

# ============================================================
# Programa: Cálculo de descuento por monto de compra
# Curso: Principios de Programación 1
# Descripción: Calcula el descuento y el total a pagar
#              según el monto de la compra.
# ============================================================


# Constantes de los límites de compra
LIMITE_DESCUENTO_1 = 30000
LIMITE_DESCUENTO_2 = 60000
LIMITE_DESCUENTO_3 = 100000


# Porcentajes de descuento
DESCUENTO_5 = 0.05
DESCUENTO_10 = 0.10
DESCUENTO_15 = 0.15


# Entrada de datos
monto_compra = float(input("Ingrese el monto de la compra: ₡"))


# Determinar el porcentaje de descuento
if monto_compra < LIMITE_DESCUENTO_1:
    porcentaje_descuento = 0
elif monto_compra < LIMITE_DESCUENTO_2:
    porcentaje_descuento = DESCUENTO_5
elif monto_compra < LIMITE_DESCUENTO_3:
    porcentaje_descuento = DESCUENTO_10
else:
    porcentaje_descuento = DESCUENTO_15


# Calcular el descuento y el total
descuento = monto_compra * porcentaje_descuento
total_pagar = monto_compra - descuento


# Mostrar resultados
print("Monto de la compra: ₡", monto_compra)
print("Descuento aplicado: ₡", descuento)
print("Total a pagar: ₡", total_pagar)
