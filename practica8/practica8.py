import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../athlete_events.csv')

df.dropna(subset=['Height', 'Weight', 'Age', 'Medal', 'Year'], inplace=True)

x = df[['Age', 'Height', 'Weight', 'Year']]
y = df['Medal']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy}")

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Valores Pronosticados')
plt.ylabel('Valores Reales')
plt.title('Matriz de Confusión')
plt.savefig('matriz_confusion.png')
plt.show()

pred_counts = pd.Series(y_pred).value_counts()
plt.figure(figsize=(8, 6))
pred_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Categoría Pronosticada')
plt.ylabel('Cantidad')
plt.title('Distribución de Categorías Pronosticadas')
plt.xticks(rotation=45)
plt.savefig('distribucion_categorias.png') 
plt.show()

nuevos_datos = pd.DataFrame({'Age': [30], 'Height': [180], 'Weight': [75], 'Year': [2025]})
pronostico = modelo.predict(nuevos_datos)
print(f"Pronóstico: {pronostico}")
