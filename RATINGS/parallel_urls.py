from joblib import Parallel, delayed
from selenium import webdriver
import pandas as pd
import time
path = "/Users/cerivera/Downloads/chromedriver_mac_arm64/chromedriver"
def abrirMubiUrl(url: str)-> str: 
    if type(url) is str: 
        driver = webdriver.Chrome(path)
        driver.get(url)
        #time.sleep(1)
        driver.quit()
    return url
data = pd.read_csv("/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexasconmubilink.csv", sep=",", encoding="utf-8")
lista = data['urlmubi'].dropna().to_list()
t1 = time.time()
for url in lista[:10]:
    abrirMubiUrl(url)
t2 = time.time()
print(f'El tiempo de ejecucion sin paralelización fue de {t2-t1} segundos')


t1 = time.time()
Parallel(n_jobs=-1)(delayed(abrirMubiUrl)(url) for url in lista[:10])
t2 = time.time()
print(f'El tiempo de ejecucion con paralelización fue de {t2-t1} segundos')