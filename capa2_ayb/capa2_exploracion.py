import pandas as pd
import sys
import os

# 1. Conexión entre carpetas: Agregar la ruta raíz al sistema para poder importar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from capa1_union.capa1_union import ventas_clientes

datos = ventas_clientes.copy()

print("\n--- DIAGNÓSTICO DE ERRORES (ACTIVIDAD 2A) ---")

# 1. Filas repetidas
print(f"Filas repetidas encontradas: {datos.duplicated().sum()}")

# 2. Valores nulos (vacíos)
print("\nValores nulos por columna:")
print(datos.isna().sum())

# 3. Categorías de producto
print("\nCategorías de producto identificadas:")
print(datos["categoria"].unique())

# 4. Ciudades del cliente
print("\nCiudades del cliente identificadas:")
print(datos["ciudad_y"].unique())

# 5. Tipos de datos (para detectar columnas numéricas/fechas que se leen como texto)
print("\nTipos de datos actuales:")
print(datos.dtypes)

# 6. Muestra de fechas para ver el formato
print("\nMuestra de fechas (nota los distintos formatos):")
print(datos["fecha"].dropna().head(5).tolist())

# 7. Cantidad mínima vendida
print(f"\nCantidad mínima vendida detectada: {datos['cantidad'].min()}")