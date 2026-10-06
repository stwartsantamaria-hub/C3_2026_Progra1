"""
Situación planteada:
Una tienda desea calcular cuánto debe pagar un cliente por un producto. 
El programa debe solicitar el nombre del producto, el precio unitario y la cantidad de unidades.
Con estos datos, el programa debe calcular el total a pagar y mostrar la información al usuario.

NombrePrd = input("Ingrese el nombre del producto:")
PrecioUnit = float (input("Ingrese el precio unitario:"))
Qty = int (input("Ingrese la cantidad de unidades:"))
print("El total a cancelar es de:", PrecioUnit*Qty)
print("fin del programa!!")
"""

"""
¿Qué hay de nuevo en este formato?

total_a_pagar = ...: El cálculo queda separado de la impresión en pantalla.
f"Texto {variable}": Anteponer una f antes de las comillas permite meter variables dentro de las llaves {} directamente sin usar comas.
{total_a_pagar:.2f}: El :.2f le indica a Python que muestre el número siempre con exactamente 2 decimales (muy útil para montos de dinero).
"""
# 1. Entrada de datos
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad de unidades: "))

# 2. Proceso: calcular el total a pagar y almacenarlo en su variable
total_a_pagar = precio_unitario * cantidad

# 3. Salida de datos usando f-strings
print(f"\n--- RESUMEN DE COMPRA ---")
print(f"Producto: {nombre_producto}")
print(f"Cantidad: {cantidad}")
print(f"El total a cancelar por el producto {nombre_producto} es: ₡{total_a_pagar:.5lelf}")

# 4. Fin
print("¡Fin del programa!")