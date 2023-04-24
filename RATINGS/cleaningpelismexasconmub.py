import pandas as pd
import numpy as np

data = pd.read_csv(
            "/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexasconmubilinkverified.csv",
            sep=",",
            encoding="utf-8",
        )
copia = data
copia.loc[copia["Urlverification"] == 0, "urlmubi"] = np.nan
listaurls = copia["urlmubi"].dropna().tolist()
print(len(listaurls))
linksconrating = pd.read_csv("/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/mubiratingscrapper.csv", sep=",", encoding="utf-8")
errores = []
listalinksconsultados = linksconrating["urlmubi"].tolist()
for url in listaurls:
    if url not in listalinksconsultados:
        errores.append(url)
print(errores)
merged_df = pd.merge(copia, linksconrating, on="urlmubi", how="left")
merged_df.drop(columns= ["Urlverification", 'urlmubi'], inplace=True)
merged_df.columns = ['Film', 'Director', 'mubi_rating']

#merged_df.to_csv("/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/pelismexasconmubirating.csv", sep=",", encoding="utf-8", index=False)
data= pd.read_csv("/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/pelismexasconmubirating.csv", sep=",", encoding="utf-8")
original = pd.read_csv("/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexas2016-2021.csv", sep=",", encoding="utf-8")
listaoriginal = original["Film"].tolist()
listamerged = data["Film"].tolist()
print(len(listamerged) - len(listaoriginal))
# Hay peliculas repetidas
yapaseestapeli = {}
for film in listaoriginal: 
    yapaseestapeli[film] = False

for film in listamerged:
    if yapaseestapeli[film]:
        print(f'la peli duplicada es: {film}')
    yapaseestapeli[film] = True



