# -*- coding: utf-8 -*-
"""
Created on Tue May 10 20:28:54 2022

@author: Rjove
"""

from CONFIG_GERAL import *

contatos= []
grupos = []
EM_ATENDIMENTO = []

with open ('{}/CONFIGS/MSG_SAUDACAO.txt'.format(RAIZ),'r',encoding='utf8') as f:
    MSG_SAUDACAO = f.read()
    
path.insert(1, r"{}/COMPONENTES".format(RAIZ)) 
from WHATSAPP_BOT import *



