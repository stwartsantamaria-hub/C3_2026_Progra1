# ==============================================================================
# Nombre del estudiante: Stwart Santamaria Artavia
# Contexto seleccionado: Problema 1. Cajero automático
# Descripción: Simula retiros consecutivos en un cajero automático sobre un
#              saldo inicial de ₡250 000 utilizando un ciclo while.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CONSTANTES
# ------------------------------------------------------------------------------
SALDO_INICIAL = 250000.0   # Saldo inicial fijado por la regla de negocio
RETIRO_MINIMO = 5000.0     # Retiro mínimo por operación
RETIRO_MAXIMO = 100000.0   # Retiro máximo por operación
OPCION_CONTINUAR = "s"     # Opción afirmativa para continuar

# ------------------------------------------------------------------------------
# 2. INICIALIZACIÓN DE VARIABLES Y MUESTREO INICIAL
# ------------------------------------------------------------------------------
saldo = SALDO_INICIAL
retiros_exitosos = 0
monto = 0.0

# Muestra del saldo disponible inicial
print("==========================================")
print("       BIENVENIDO AL CAJERO AUTOMÁTICO    ")
print("==========================================")
print("Saldo disponible inicial: ₡", saldo)

# Pregunta inicial para evaluar el ingreso al ciclo (Permite 0 iteraciones)
continuar = input("¿Desea realizar una operación de retiro? (s/n): ")

# ------------------------------------------------------------------------------
# 3. CICLO ITERATIVO WHILE
# ------------------------------------------------------------------------------
while continuar.lower() == OPCION_CONTINUAR and saldo >= RETIRO_MINIMO:
    
    # Lectura del monto a retirar en cada operación
    monto = float(input("\nIngrese el monto a retirar: ₡"))

    # Rombo 1: Validación de Límites (₡5 000 a ₡100 000)
    if monto >= RETIRO_MINIMO and monto <= RETIRO_MAXIMO:
        
        # Rombo 2: Validación de Fondos Disponibles
        if monto <= saldo:
            # Procesos cuando el retiro es exitoso
            saldo = saldo - monto
            retiros_exitosos = retiros_exitosos + 1
            print("Estado: Retiro REALIZADO con éxito.")
        else:
            # Mensaje cuando el monto supera el saldo disponible
            print("Estado: Retiro NO realizado (Error: Fondos insuficientes).")
            
    else:
        # Mensaje cuando el monto no cumple con el rango mínimo/máximo
        print("Estado: Retiro NO realizado (Error: El monto debe estar entre ₡5 000 y ₡100 000).")

    # Muestra del saldo actualizado por cada intento
    print("Saldo actualizado: ₡", saldo)

    # Evaluación para solicitar la confirmación de continuar
    if saldo >= RETIRO_MINIMO:
        continuar = input("¿Desea realizar otro retiro? (s/n): ")
    else:
        print("\nSaldo insuficiente para realizar más retiros (mínimo ₡5 000).")
        continuar = "n"

# ------------------------------------------------------------------------------
# 4. SALIDA FINAL DE RESULTADOS
# ------------------------------------------------------------------------------
print("\n------------------------------------------")
print("             RESUMEN FINAL                ")
print("------------------------------------------")
print("Saldo restante final : ₡", saldo)
print("Total retiros exitosos:", retiros_exitosos)
print("[Fin de la operación]")