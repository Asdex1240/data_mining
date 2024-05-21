import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Carga los datos desde el archivo CSV
ruta_archivo_limpios = '../athlete_events.csv'
df = pd.read_csv(ruta_archivo_limpios)

# Eliminar filas con valores NaN en 'Height' y 'Weight'
df = df.dropna(subset=['Height', 'Weight'])

# Variables independientes (X) y dependientes (y)
altura = df['Height'].values.reshape(-1, 1)
peso = df['Weight'].values

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo
modelo.fit(altura, peso)

# Predecir los pesos usando el modelo ajustado
predicciones_peso = modelo.predict(altura)

# Crear el gráfico
plt.scatter(altura, peso, color='blue', label='Datos reales')
plt.plot(altura, predicciones_peso, color='red', linewidth=2, label='Línea de Regresión')
plt.title('Regresión Lineal: Altura vs Peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.grid(True)

# Guardar la imagen en un archivo
plt.savefig('regresion_altura_vs_peso.png')

# Mostrar la imagen
plt.show()
