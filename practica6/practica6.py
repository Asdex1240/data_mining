import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('../athlete_events.csv')

# Selecciona el país que deseas analizar
pais_seleccionado = 'Australia' 

# Filtra los datos para el país seleccionado
datos_pais = df[df['Team'] == pais_seleccionado]

# Agrupa los datos por año y cuenta el número de entradas por año
clasificacion_por_anio = datos_pais['Year'].value_counts().sort_index()

# Crea un gráfico de barras para mostrar la clasificación por año
plt.figure(figsize=(10, 6))
clasificacion_por_anio.plot(kind='bar', color='skyblue')
plt.title(f'Clasificación por Año para {pais_seleccionado}')
plt.xlabel('Año')
plt.ylabel('Número de Participantes')
plt.xticks(rotation=45)

# Guarda la imagen en un archivo
plt.savefig('clasificacion_por_anio.png')

# Muestra el gráfico
plt.show()
