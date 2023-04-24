from pathlib import Path

import scrapy
import pandas as pd
import numpy as np
import logging


class RatingsSpider(scrapy.Spider):
    name = "ratings"

    def start_requests(self):
        data = pd.read_csv(
            "/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/peliculasmexasconmubilinkverified.csv",
            sep=",",
            encoding="utf-8",
        )
        # print(data['Urlverification'].eq(1).sum())
        copia = data
        copia.loc[copia["Urlverification"] == 0, "urlmubi"] = np.nan
        listaurls = copia["urlmubi"].dropna().tolist()
        urls = listaurls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        logging.basicConfig(
            filename="/Users/cerivera/Documents/ProyectoCineMexicano/erroresscraping.log",
            level=logging.ERROR,
        )
        #rating = response.css("body").re('css-1g9erbj\se1tkkgq82">...')
        try:
            rating = response.xpath('//*[@id="__next"]/div[1]/div[4]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]').re("\d\.\d")
        except Exception as e:
            logging.error(
                f"Ocurrio el error{e} al momento de cargar la pagina {response.url}"
            )
            rating = 0
        path = "/Users/cerivera/Documents/ProyectoCineMexicano/RATINGS/mubiratingscrapper_copy.csv"
        with open(path, "a") as f:
            resp = str(response.url) + "," + str(rating) + "\n"
            f.write(resp)
