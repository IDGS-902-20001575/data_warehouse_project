import pandas as pd

# Cargar dataset
df = pd.read_csv('dataset_limpio.csv')

# Estadísticas generales
print("Resumen estadístico:")
print(df.describe())

# Análisis de abandono
print("\nTasa de abandono:")
print(df['abandono'].mean())

# Abandono por tipo de plan
print("\nAbandono por tipo de plan:")
print(df.groupby('plan_servicio')['abandono'].mean())

# Relación entre satisfacción y abandono
print("\nPromedio de satisfacción por abandono:")
print(df.groupby('abandono')['puntaje_satisfaccion'].mean())

# Clientes con mayor riesgo (baja satisfacción)
riesgo = df[df['puntaje_satisfaccion'] < 6]
print("\nClientes en riesgo de abandono:")
print(riesgo)
