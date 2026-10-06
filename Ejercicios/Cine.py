# ==========================================
# SISTEMA DE CÁLCULO DE ENTRADAS DE CINE
# ==========================================
'''
# CONSTANTES
PRECIO_ENTRADA = 3500  

# ENTRADA DE DATOS (Solicitados al usuario)
edad = int(input("Ingrese la edad del cliente: "))
cantidad_entradas = int(input("Ingrese la cantidad de entradas: "))

# CÁLCULO DEL SUBTOTAL
subtotal = PRECIO_ENTRADA * cantidad_entradas

# ESTRUCTURA CONDICIONAL: DETERMINAR DESCUENTO POR EDAD
if edad < 12:
    porcentaje_descuento = 0.20
elif edad >= 65:
    porcentaje_descuento = 0.15
else:
    porcentaje_descuento = 0.00

# CÁLCULOS MONETARIOS FINALES
monto_descuento = subtotal * porcentaje_descuento
total_a_pagar = subtotal - monto_descuento

# ESTRUCTURA CONDICIONAL: BEBIDA GRATIS
if cantidad_entradas >= 4:
    mensaje_bebida = "¡Aplica para 1 bebida GRATIS!"
else:
    mensaje_bebida = "No aplica para bebida gratis"

# 7. SALIDA DE DATOS / MOSTRAR RESULTADOS
print("\n--- RESUMEN DE LA COMPRA ---")
print(f"Subtotal: ₡{subtotal:,.2f}")
print(f"Descuento aplicado: ₡{monto_descuento:,.2f}")
print(f"Total a pagar: ₡{total_a_pagar:,.2f}")
print(f"Regalo: {mensaje_bebida}")
'''
# =========================================================
# Ejercicio: Cálculo de entradas de cine
# Estilo de solución: Secuencial con estructuras condicionales
# =========================================================

# CONSTANTES
PRECIO_ENTRADA = 3500
ANCHO_BARRA_FORMATO = 40

# 1. Entrada de datos
edad = int(input("Ingrese la edad del cliente: "))
cantidad_entradas = int(input("Ingrese la cantidad de entradas: "))

# 2. Proceso: Cálculo del subtotal
subtotal = cantidad_entradas * PRECIO_ENTRADA

# Proceso: Determinación del porcentaje de descuento según edad
if edad < 12:
    porcentaje_descuento = 0.20
elif edad >= 65:
    porcentaje_descuento = 0.15
else:
    porcentaje_descuento = 0.00

# Proceso: Cálculo del monto final de descuento y total a pagar
monto_descuento = subtotal * porcentaje_descuento
total_pagar = subtotal - monto_descuento

# Proceso: Verificación de la regalía de bebida
if cantidad_entradas >= 4:
    bebida_gratis = "¡Incluye 1 bebida gratis!"
else:
    bebida_gratis = "No aplica para bebida gratis."

# 3. Salida de datos
print("\n" + "=" * ANCHO_BARRA_FORMATO)
print("        FACTURA / RESUMEN DE COMPRA")
print("=" * ANCHO_BARRA_FORMATO)
print(f"Subtotal:          CRC {subtotal:.2f}")
print(f"Descuento ({int(porcentaje_descuento * 100)}%):  CRC {monto_descuento:.2f}")
print(f"Total a pagar:     CRC {total_pagar:.2f}")
print("-" * ANCHO_BARRA_FORMATO)
print(f"Regalía:           {bebida_gratis}")
print("=" * ANCHO_BARRA_FORMATO)