# -*- coding: utf-8 -*-
"""
Created on Fri May 13 20:09:06 2022

@author: Rjove
"""
from CONFIG_GERAL import *

JOVEPY= Tk()
JOVEPY.title("JOVEPY - EMPREENDA")
JOVEPY.geometry("500x200")
#JOVEPY.wm_iconbitmap(r'logo.ico')
JOVEPY['bg']='LightSteelBlue'

Button(
    JOVEPY, height=2,
    text="ATENDER", 
    command=ROTINA_ATENDIMENTO,
    ).pack(side=TOP, expand=True, fill=X, padx=20)

Button(
    JOVEPY, height=2,
    text="PESQUISA DE PREÇO", 
    ).pack(side=TOP, expand=True, fill=X, padx=20)

Button(
    JOVEPY, height=2,
    text="ENVIAR PROMOÇÃO", 
    ).pack(side=TOP, expand=True, fill=X, padx=20)

Button(
    JOVEPY, height=2,
    text="DASHBOARD", 
    ).pack(side=TOP, expand=True, fill=X, padx=20)

JOVEPY.mainloop()