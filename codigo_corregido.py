from selenium.webdriver.support import expected_conditions
from seleniumbase import Driver
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from selenium.webdriver.common.by import By
import pandas as pd
from PrettyColorPrinter import add_printer
import threading
add_printer(1)
drivers = {}

def abrir_site(nome,q,with_methods):
    def g():  # adicionando o parâmetro driver e mudando o valor padrão de q para "a"
        return get_df(drivers[nome], By, WebDriverWait, expected_conditions, queryselector=q, with_methods=with_methods, )
    drivers[nome].get(nome)  # usando a variável nome para acessar o dicionário drivers
    df=pd.DataFrame()
    while df.empty:
        df = g()
    resultados.append(df)


nomes = [
    "https://www.google.com",
    "https://www.uol.com.br",

]
for nome in nomes:
    drivers[nome] = Driver(uc=True)

resultados = []


for nome in nomes:
    try:
        threading.Thread(target=abrir_site, args=(nome,'a',True)).start()
    except Exception as e:
        print(e)
        continue
