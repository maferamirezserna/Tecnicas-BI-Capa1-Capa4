import pandas as pd

# 1. Leer el Excel
ventas = pd.read_excel("C:\\Trabajo_BI\\Datos\\ventas.xlsx")

# 2. Leer el CSV
clientes = pd.read_csv("C:\\Trabajo_BI\\Datos\\clientes.csv", sep=";")

# 1. ¿Cuántas filas y columnas tiene cada archivo?
# R/ Ventas tiene 420 filas y 9 columnas. Clientes tiene 65 filas y 4 columnas.

# 2. ¿Qué pasa si haces pd.read_csv sin nada más? ¿Por qué?
# R/ Lee todo como si fuera una sola columna, porque pandas asume por defecto que el separador es la coma (,).

# 3. ¿Cuál es el separador real del CSV? ¿Cómo te diste cuenta?
# R/ El separador es el punto y coma (;). Se evidencia al abrir el archivo en bloc de notas o al ver que pandas no separa las columnas.

# 3. Unir las dos tablas
ventas_clientes = pd.merge(ventas, clientes, on="id_cliente", how="left")
# 4. ¿Por qué columna se unen las dos tablas?
# R/ Se unen por la llave en común: 'id_cliente'.

# 5. ¿Qué tipo de unión usaste y por qué?
# R/ Usamos un 'left' join (izquierda) porque nuestra base principal son las transacciones (ventas) y queremos traer los datos del 
# cliente sin perder ninguna venta, incluso si el cliente no aparece en el CSV.

# 4. Imprimir el número de filas
print(f"Filas de ventas: {len(ventas)}")
print(f"Filas de clientes: {len(clientes)}")
print(f"Filas del resultado: {len(ventas_clientes)}")

# 6. ¿Cuántas filas tenía ventas antes de unir y cuántas quedaron después?
# R/ Ventas tenía 420 filas. Después de unir quedaron 453 filas.

# 7. Si el número cambió, ¿por qué cambió?
# R/ Aumentó porque en el archivo clientes.csv hay 'id_cliente' repetidos. Al cruzar los datos, las ventas asociadas a esos clientes 
# duplicados se multiplican (producto cartesiano).