import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn import metrics

# Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv('../athlete_events.csv')

# Eliminar filas con valores faltantes en las columnas de interés
df.dropna(subset=['Height', 'Weight', 'Age'], inplace=True)

# Seleccionar las características para la regresión lineal
x = df[['Height', 'Weight']]
y = df['Age']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Crear un modelo de regresión lineal con un pipeline que incluye imputación y escala
modelo = make_pipeline(SimpleImputer(strategy='mean'), StandardScaler(), LinearRegression())

# Ajustar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Evaluar el rendimiento del modelo
print('Error absoluto medio:', metrics.mean_absolute_error(y_test, y_pred))
print('Error cuadrático medio:', metrics.mean_squared_error(y_test, y_pred))
print('Raíz del error cuadrático medio:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# Graficar la regresión lineal y los datos reales
plt.scatter(X_test['Height'], y_test, color='black', label='Datos reales')
plt.scatter(X_test['Height'], y_pred, color='blue', linewidth=3, label='Predicciones')
plt.title('Regresión Lineal: Edad en función de Altura y Peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Edad')
plt.legend()

# Guardar la imagen como un archivo
plt.savefig('regresion_lineal_edad_altura_peso.png')

# Mostrar la gráfica
plt.show()

# Ahora, puedes utilizar el modelo para predecir la edad en base a la altura y el peso de un atleta específico
nueva_data = pd.DataFrame({'Height': [180], 'Weight': [75]})
prediccion_nueva = modelo.predict(nueva_data)

print(f'Predicción de edad para una altura de 180 cm y peso de 75 kg: {prediccion_nueva[0]} años')
