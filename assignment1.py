import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

df = pd.read_csv("IMDB.csv")                        #Carico il dataframe IMDB
pd.set_option('expand_frame_repr', False)           #Funzione per visualizzare il dataframe per esteso sulla console
print(df.head(10))                                  #Visualizzo in console le prime 10 righe del dataframe

#Definisco un dizionario vuoto in cui le CHIAVI sono i nomi
# #delle colonne di tipo int o float e i VALORI sono il tipo di dato
column_dtype = {}

#Con questa funzione sostituisco gli zeri nelle colonne numeriche
#con un NaN


def zero_to_nan(df,a):
    for columns in df:
        if df[columns].dtype == 'int64':
            df[columns] = df[columns].replace(0, np.nan)
            a[columns] = 'int'
        elif df[columns].dtype == 'float64':
            df[columns] = df[columns].replace(0, np.nan)
            a[columns] = 'float'
    return df


#Con questa funzione rimpiazzo tutti i Nan nelle colonne numeriche con la mediana delle colonne
#forzando il tipo di dato nella colonna con astype per un output migliorato, mantenendo l'originalità del Dataframe


def replace_nan(df,a):
    for columns in a:
        df[columns] = df[columns].replace(np.nan, np.nanmedian(df[columns])).astype(a[columns])
    return df

#Opero sul dataframe con le funzioni costruite e con delle funzioni pandas


df = zero_to_nan(df, column_dtype)
df.dropna(axis=0, thresh=4)                         #Elimino le righe con più di 4 valori NaN
df = replace_nan(df, column_dtype)
df = df.dropna(axis=0)                              #Elimino tutte le righe che hanno stringhe nulle:
                                                    #Scelta più "aggressiva"
print(df.head(10))
#Salvo il dataframe pulito in un csv
df.to_csv('clear_data.csv')

#Opzionale: Abbiamo deciso di plottare alcune statistiche relative agli incassi

#Analizziamo il dataframe pulito

df = pd.read_csv('clear_data.csv')

revenue = {}                               #Chiave = anno  , Valore = somma di tutti i guadagni per anno
for i in range(len(df.index)):
    if df['Year'][i] not in revenue:
        revenue[df['Year'][i]] = df['Revenue (Millions)'][i]
    else:
        revenue[df['Year'][i]] += df['Revenue (Millions)'][i]

List_1 = revenue.items()
List_1 = sorted(List_1)
x, y = zip(*List_1)

plt.plot(x, y)
plt.xlabel('Year')
plt.ylabel('Total Revenue')
plt.show()

sns.catplot(x='Year', y='Revenue (Millions)', kind='box', data=df)
plt.show()

