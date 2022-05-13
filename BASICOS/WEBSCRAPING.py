# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:45:38 2022

@author: rodrigo.jove
"""

from config_empreendedor import *

def navegar_chrome():
    global driver    
    chrome_options =webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    #ua = UserAgent()
    #userAgent = ua.random
    #chrome_options.add_argument(f'user-agent={userAgent}')
    prefs = {"download.default_directory" : '{}\Programa para Empreendedores\Arquivos\Downloads'.format(RAIZ)} #LOCAL ONDE SEMPRE SERÁ BAIXADO OS ARQUIVOS, SEMPRE SERÃO APAGADOS APÓS O USO, SÓ É PARA TER UM ARQUIVO NESSA PASTA
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    driver =  webdriver.Chrome('{}/Programa para Empreendedores/Dependencias/chromedriver.exe'.format(RAIZ),options=chrome_options) #service=Service(ChromeDriverManager().install())
    driver.set_window_position(0,0)
    driver.set_window_size(1600, 800)
    return(driver)

def retorna_back(driver):
    page_content= driver.page_source 
    back = bs(page_content, 'html.parser')
    return(back)

