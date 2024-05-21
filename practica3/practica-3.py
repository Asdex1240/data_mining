import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def maxMedallas(df, save_path='max_medallas.png'):
    df_cleaned = df.dropna(subset=['Medal'])
    medallas_por_ciudad = df_cleaned.groupby(['City', 'Name']).size().reset_index(name='Numero_Medallas')
    atletas_mas_medallas = medallas_por_ciudad.loc[medallas_por_ciudad.groupby('City')['Numero_Medallas'].idxmax()]
    atletas_mas_medallas_sorted = atletas_mas_medallas.sort_values(by='Numero_Medallas', ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Numero_Medallas', y='City', data=atletas_mas_medallas_sorted, estimator=sum)
    plt.title('Número total de medallas por ciudad (ordenado de mayor a menor)')
    plt.xlabel('Número total de medallas')
    plt.ylabel('Ciudad')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def medallas_por_edad(df, save_path='medallas_por_edad.png'):
    df_con_medallas = df.dropna(subset=['Medal'])
    medallas_por_edad = df_con_medallas.groupby('Age').size().reset_index(name='Numero_Medallas')
    medallas_por_edad_ordenadas = medallas_por_edad.sort_values(by='Numero_Medallas', ascending=False)
    plt.figure(figsize=(12, 6))
    plt.bar(medallas_por_edad_ordenadas['Age'], medallas_por_edad_ordenadas['Numero_Medallas'], color='skyblue')
    plt.title('Número de medallas por edad')
    plt.xlabel('Edad')
    plt.ylabel('Número de medallas')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def mejores_5_medallas_de_oro(df, save_path='mejores_5_medallas_de_oro.png'):
    df_oro = df[df['Medal'] == 'Gold']
    medallas_oro_por_atleta = df_oro.groupby('Name').size().reset_index(name='Numero_Medallas_Oro')
    mejores_5 = medallas_oro_por_atleta.sort_values(by='Numero_Medallas_Oro', ascending=False).head(5)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Numero_Medallas_Oro', y='Name', data=mejores_5)
    plt.title('Mejores 5 atletas con medallas de oro')
    plt.xlabel('Número de medallas de oro')
    plt.ylabel('Nombre del atleta')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def estGeneral(df, save_path='estadisticas_generales.png'):
    estadisticas_generales = df.describe()
    plt.figure(figsize=(10, 6))
    estadisticas_generales.plot(kind='bar', ax=plt.gca())
    plt.title('Estadísticas Generales')
    plt.ylabel('Valor')
    plt.xlabel('Estadísticas')
    plt.legend(loc='upper right')
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def main():
    file = 'athlete_events.csv'
    df = pd.read_csv(file)
    maxMedallas(df)
    mejores_5_medallas_de_oro(df)
    estGeneral(df)
    medallas_por_edad(df)

main()
