#!/usr/bin/env python3

""" Hello Python

Como usar:
    Ter a variável LANG devidamente configurada
        LANG=pt_BR

Execução: 
    python3 hello.py ou ./hello.py
"""

__version__ = "0.0.1"
__author__ = "Uítalo Souza"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG")[:5]
msg = "hello Python"


if current_language == "pt_BR":
    msg = "olá, Python"
elif current_language == "it_IT":
    msg = "ciao, Python"

print(msg)