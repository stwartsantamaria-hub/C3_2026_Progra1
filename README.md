# Tarea 2: Cajero Automático - Principios de Programación 1 (SOFT-01)

**Universidad CENFOTEC**  
**Escuela de Ingeniería del Software**  
**Estudiante:** Stwart Santamaria Artavia  
**Curso:** Principios de Programación 1 (SOFT-01)  
**Periodo:** 2026-C3  

---

## 📌 Descripción del Proyecto

Este repositorio contiene la solución algorítmica y en código para el **Problema 1: Cajero Automático**. 

El programa simula el funcionamiento de un cajero automático en consola utilizando Python y aplicando una estructura iterativa de control `while`. Permite al usuario realizar múltiples retiros consecutivos sobre un saldo inicial fijo de **₡250 000**, aplicando validaciones estrictas de límites y fondos disponibles en cada intento.

### ⚙️ Reglas de Negocio Aplicadas
* **Saldo Inicial:** Fixed en ₡250 000.0.
* **Monto Mínimo por Retiro:** ₡5 000.0.
* **Monto Máximo por Retiro:** ₡100 000.0.
* **Control de Iteración:** El ciclo continúa únicamente si el usuario confirma continuar (`"s"`) y el saldo disponible es mayor o igual al monto mínimo (₡5 000.0).
* **Bloqueo Automático:** Si el saldo cae por debajo de ₡5 000.0, el sistema notifica la insuficiencia de fondos y finaliza el ciclo automáticamente.

---

## 📁 Estructura del Repositorio

* `main.py` - Código fuente ejecutable en Python.
* `README.md` - Documentación del proyecto e instrucciones de uso.
* `diagrama_flujo.drawio` - Diagrama de flujo editable para draw.io.
