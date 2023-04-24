import time
from selenium import webdriver
import pandas as pd
import numpy as np
path = "/Users/cerivera/Downloads/chromedriver_mac_arm64/chromedriver"
def abrirMubiUrl(url: str)-> str: 
    if type(url) is str: 
        driver = webdriver.Chrome(path)
        driver.get(url)
        time.sleep(1)
        driver.quit()
    return url


#data = pd.read_csv("/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/pelismexasconmubirating.csv", sep=",", encoding="utf-8")
#print(data['mubi_rating'].isna().sum())
data = pd.read_csv("/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexasconmubilink.csv", sep=",", encoding="utf-8")
lista = data['urlmubi'].dropna().to_list()
print(lista)