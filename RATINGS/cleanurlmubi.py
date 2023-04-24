import pandas as pd
import numpy as np

df = pd.read_csv('/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexasconmubilink.csv', sep=',', encoding='utf-8')

def cleanUrlMubi(url: str) -> str:
    if url is not np.nan:
        if url.startswith('https://mubi.com/'):
            return url
        else: 
            return None
    else: 
        return None

df['urlmubi'] = df['urlmubi'].apply(cleanUrlMubi)
print(df['urlmubi'].isna().sum())

#df.to_csv('/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexasconmubilink.csv', sep=',', encoding='utf-8', index=False)
from selenium import webdriver
import time
path = "/Users/cerivera/Downloads/chromedriver_mac_arm64/chromedriver"
def abrirMubiUrl(url: str)-> str: 
    if type(url) is str: 
        driver = webdriver.Chrome(path)
        driver.get(url)
        time.sleep(2)
        driver.quit()
    return url

#df['urlmubi'].apply(abrirMubiUrl)

data = pd.read_csv("/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexasconmubilinkverified.csv", sep=',', encoding='utf-8')
#print(data['Urlverification'].eq(1).sum())
copia = data
copia.loc[copia['Urlverification'] == 0, 'urlmubi'] = np.nan
listaurls = copia['urlmubi'].dropna().tolist()


