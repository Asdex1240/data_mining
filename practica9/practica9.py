import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


ruta_archivo_limpios = '../athlete_events.csv'
df = pd.read_csv(ruta_archivo_limpios)

print(df.head())


nombre_columna_texto = 'Sport'  
texto_para_wordcloud = ' '.join(df[nombre_columna_texto].dropna())


wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_para_wordcloud)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('nube_de_palabras.png')
plt.show()

