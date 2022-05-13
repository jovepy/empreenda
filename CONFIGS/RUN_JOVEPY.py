# -*- coding: utf-8 -*-
"""
Created on Tue May 10 20:18:02 2022

@author: Jovepy 


Esse é o módulo de execução de todo o programa. A espinha dorsal de toda estrutura.

Todos os ramos do projeto devem se unir aqui

Agregue valor à sociedade.

"""


from os import getcwd

RAIZ = '/'.join(getcwd().replace('\\','/').split('/')[:-1])
from CONFIG_GERAL import *