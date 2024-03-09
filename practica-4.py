import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


ruta_archivo_limpios = 'athlete_events.csv'
df = pd.read_csv(ruta_archivo_limpios)


def perform_anova(df, variable_dependiente, variable_independiente):
    modelo_anova = ols(f'{variable_dependiente} ~ {variable_independiente}', data=df).fit()
    tabla_anova = anova_lm(modelo_anova)
    return tabla_anova


while True:
    print("\nMenú ANOVA:")
    print("1. Comparación de edades entre deportes")
    print("2. Efecto del género en el peso")
    print("3. Comparación de alturas por medallas")
    print("4. Comparación de edades en diferentes temporadas")
    print("5. Salir")
    choice = input("Selecciona una opción: ")

    if choice == '1':
        tabla_anova = perform_anova(df, 'Age', 'Sport')
        print("\nTabla de ANOVA para la comparación de edades entre deportes:")
        print(tabla_anova)
    elif choice == '2':
        tabla_anova = perform_anova(df, 'Weight', 'Sex')
        print("\nTabla de ANOVA para el efecto del género en el peso:")
        print(tabla_anova)
    elif choice == '3':
        tabla_anova = perform_anova(df, 'Height', 'Medal')
        print("\nTabla de ANOVA para la comparación de alturas por medallas:")
        print(tabla_anova)
    elif choice == '4':
        tabla_anova = perform_anova(df, 'Age', 'Season')
        print("\nTabla de ANOVA para la comparación de edades en diferentes temporadas:")
        print(tabla_anova)
    elif choice == '5':
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")