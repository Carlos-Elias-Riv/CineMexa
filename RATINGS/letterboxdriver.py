from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from joblib import Parallel, delayed
import pandas as pd
website = "https://www.google.com/"


def getIMDBUrl(peli: str) -> str:
    path = "/Users/cerivera/Downloads/chromedriver_mac_arm64/chromedriver"
    peli = peli.lower()
    driver = webdriver.Chrome(path)
    driver.get(website)
    time.sleep(2)
    try: 
        search_button = driver.find_element_by_xpath('//input[@class="gLFyf"]')
    except: 
        search_button = driver.find_element_by_xpath('//textarea[@class="gLFyf"]')
    search_button.send_keys(f'{peli} letterboxd')
    search_button.send_keys(Keys.ENTER)
    # Path para mubi
    try: 
        #match = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/div/a')
        match = driver.find_elements_by_xpath("//h3[@class='LC20lb MBeuO DKV0Md']")[0]
        match.click()
        resp = driver.current_url
        driver.quit()
        
        return resp
    except: 
        driver.quit()
        
        return None

data = pd.read_csv('/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexas2016-2021.csv')
pelis = data['Film'].to_list()

urls = Parallel(n_jobs=6)(delayed(getIMDBUrl)(peli) for peli in pelis)

data['letterboxdurl'] = urls
data.to_csv('/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/pelismexasconletterboxd.csv', sep=',', encoding='utf-8', index=False)
