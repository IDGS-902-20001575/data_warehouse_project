import pandas as pd

# Load dataset
df = pd.read_csv('data/raw/dataset.csv')

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df['nombre'] = df['nombre'].fillna('Desconocido')
df['edad'] = df['edad'].fillna(df['edad'].mean())
df['fecha'] = df['fecha'].fillna('2024-01-01')

# Save cleaned dataset
df.to_csv('data/processed/dataset_clean.csv', index=False)

print("Dataset cleaned successfully!")
