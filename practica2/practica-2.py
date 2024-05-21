import pandas as pd
import numpy as np

# Cargar el archivo CSV con datos limpios
def maxMedallas(df):
    df_cleaned = df.dropna(subset=['Medal'])
    medallas_por_ciudad = df_cleaned.groupby(['City', 'Name']).size().reset_index(name='Numero_Medallas')
    atletas_mas_medallas = medallas_por_ciudad.loc[medallas_por_ciudad.groupby('City')['Numero_Medallas'].idxmax()]
    print(atletas_mas_medallas)

def mejores_5_medallas_de_oro(df):
    # Filtrar solo las medallas de oro
    df_oro = df[df['Medal'] == 'Gold']
    
    # Agrupar por nombre del atleta y contar el número de medallas de oro
    medallas_oro_por_atleta = df_oro.groupby('Name').size().reset_index(name='Numero_Medallas_Oro')
    mejores_5 = medallas_oro_por_atleta.sort_values(by='Numero_Medallas_Oro', ascending=False).head(5)
    print(mejores_5)

def main():

    file = 'athlete_events.csv'
    df = pd.read_csv(file)
    maxMedallas(df)
    mejores_5_medallas_de_oro(df)
    estGeneral(df)


def estGeneral(df):
    estadisticas_generales = df.describe()
    """

    Dentro de esta función cuenta con las siguientes columnas siguiente:

    ID, Age, Height ,Weight, Year

    De las cuales no arroja lo siguiente:

    count:  muestra el número de valores no nulos para cada columna. Por ejemplo, hay 271116 valores no nulos para la columna 'ID'.

    mean:   Es el promedio de los valores en cada columna. Por ejemplo, la altura promedio es de aproximadamente 175.34 cm.

    std:    Es la desviación estándar, que mide la dispersión de los valores alrededor de la media. Por ejemplo, la desviación estándar de la edad es aproximadamente 6.39 años.

    min:    Muestra el valor mínimo de cada columna. Por ejemplo, la edad mínima registrada es de 10 años.

    25%, 
    50%,    Son los percentiles. Por ejemplo, el 25% de los atletas tienen una altura de 168 cm o menos, el 50% tienen una altura de 175 cm o menos (la mediana) y el 75% tienen una altura de 183 cm o menos.
    75%: 

    max:    muestra el valor máximo de cada columna. Por ejemplo, la edad máxima registrada es de 97 años.

    """
    print(estadisticas_generales)


main()





