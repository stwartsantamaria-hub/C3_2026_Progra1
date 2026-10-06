# 1. Pedir información del producto
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad de unidades: "))

# 2. Calcular y mostrar el subtotal
subtotal = precio_unitario * cantidad
print(f"\nSubtotal de la compra: ${subtotal:.2f}")

# 3. Preguntar si aplica descuento (y/n)
aplica_descuento = input("¿Desea aplicar un 10% de descuento? (y/n): ").lower()

# Evaluar respuesta
if aplica_descuento == 'y':
    porcentaje_descuento = 10
else:
    porcentaje_descuento = 0

# 4. Calcular descuento y total final
monto_descuento = subtotal * (porcentaje_descuento / 100)
precio_final = subtotal - monto_descuento

# Mostrar resumen final
print("\n--- RESUMEN FINAL DE LA COMPRA ---")
print(f"Producto: {nombre_producto}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado ({porcentaje_descuento}%): -${monto_descuento:.2f}")
print(f"Total a pagar: ${precio_final:.2f}")

# Fin
print("¡Fin del programa!")