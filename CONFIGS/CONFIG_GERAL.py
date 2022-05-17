# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:00:33 2022

@author: ohmkas
"""

from RUN_JOVEPY import *

#Raspagens
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager #pip 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests

#Assistência
import pyautogui
from time import sleep
from os import listdir, chdir, mkdir, startfile, kill, system, remove
from shutil import copyfile
from sys import path
from datetime import date
from tkinter import *
from tkinter import messagebox



#Manipulação
from unicodedata import normalize
from datetime import date, timedelta
import pandas as pd
import numpy as np
import spacy


nlp = spacy.load('pt_core_news_sm')    




path.insert(1, r"../COMPONENTES") 
from WHATSAPP_BOT import *
from MENUS import *

