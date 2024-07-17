 #!/usr/bin/env python3
 
# Hello Python configurando opções de linguagem em um dicionário

__version__ = "0.1.1"
__author__ = "Uítalo Souza"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = {
    "en_US": "Hello Python",
    "pt_BR": "Olá Python",
    "it_IT": "Ciao Python",
    "fr_FR": "Bonjour Python"
}

print(msg[current_language]) 