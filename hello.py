 #!/usr/bin/env python3
 
# Hello Python passando a opção de idioma de forma dinâmica

__version__ = "0.1.2"
__author__ = "Uítalo Souza"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": None }

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid argument `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]

if current_language is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language = input("Choose a language: ")

if arguments["count"] is None:
    arguments["count"] = 1

msg = {
    "en_US": "Hello Python",
    "pt_BR": "Olá Python",
    "it_IT": "Ciao Python",
    "fr_FR": "Bonjour Python"
}

print(msg[current_language] * int(arguments["count"])) 