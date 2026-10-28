import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from capa1_union.capa1_union import ventas_clientes

datos = ventas_clientes.copy()

print("\n--- INICIO DE CAPA 2B: LIMPIEZA ---")
print(f"Filas al empezar: {len(datos)}")

# ERROR 1 y 8: Filas y clientes repetidos
# DECISIÓN: Eliminar duplicados usando 'id_venta' como llave única para solucionar tanto las ventas idénticas como la 
# multiplicación causada por los clientes duplicados.
# FILAS AFECTADAS: 53
datos = datos.drop_duplicates(subset=["id_venta"])
print(f"1 y 8) Sin filas ni clientes repetidos -> {len(datos)}")

# ERROR 2: La fecha viene en dos formatos distintos
# DECISIÓN: Estandarizar a formato universal con pd.to_datetime y el atributo dayfirst=True.
# FILAS AFECTADAS: 400
datos["fecha"] = pd.to_datetime(datos["fecha"], format="mixed", dayfirst=True, errors="coerce")

# ERROR 3: Hay ventas sin fecha
# DECISIÓN: Se dejan como nulas (NaT). Se necesita la venta para el total de facturación.
# FILAS AFECTADAS: 18 nulos
print(f"2 y 3) Fechas estandarizadas (vacías mantenidas) -> {len(datos)}")

# ERROR 4: El precio viene como texto con $
# DECISIÓN: Eliminar $, quitar puntos, espacios, y convertir a numérico.
# FILAS AFECTADAS: ~124
datos["precio_unitario"] = datos["precio_unitario"].astype(str).str.replace("$", "", regex=False).str.replace(".", "", 
    regex=False).str.strip()
datos["precio_unitario"] = pd.to_numeric(datos["precio_unitario"], errors="coerce")

# ERROR 5: Hay cantidades negativas o en cero
# DECISIÓN: Se eliminan. Sin consultar al negocio, asumimos que son errores de captura y no devoluciones.
# FILAS AFECTADAS: 13
datos = datos[datos["cantidad"] > 0]
print(f"5) Sin cantidades <= 0 -> {len(datos)}")

# ERROR 6: La categoría está escrita de varias formas
# DECISIÓN: Homologar quitando espacios y aplicando formato de Título.
# FILAS AFECTADAS: Todas
datos["categoria"] = datos["categoria"].str.strip().str.title()

# ERROR 7: Hay ventas sin ciudad
# DECISIÓN: Rellenar con "Sin ciudad" para no perder la venta ni mentir asignándole una ciudad falsa.
# FILAS AFECTADAS: 14 nulos
datos["ciudad_x"] = datos["ciudad_x"].fillna("Sin ciudad")

# ERROR 9: Hay clientes sin segmento
# DECISIÓN: Rellenar con "Sin segmento".
# FILAS AFECTADAS: 37 nulos
datos["segmento"] = datos["segmento"].fillna("Sin segmento")

# ERROR 10: La ciudad del cliente está escrita de varias formas
# DECISIÓN: Homologar aplicando formato de Título y quitando espacios.
# FILAS AFECTADAS: Todas
datos["ciudad_y"] = datos["ciudad_y"].str.strip().str.title()

# Crear columna total
datos["total"] = datos["cantidad"] * datos["precio_unitario"]

print(f"Filas limpias: {len(datos)}")
print(f"Venta total: $ {datos['total'].sum():,.0f}")