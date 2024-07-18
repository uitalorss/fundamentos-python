 #!/usr/bin/env python3
 
# Hello Python passando a opção de idioma de forma dinâmica

__version__ = "0.1.2"
__author__ = "Uítalo Souza"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1 }

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError:
        print("[Error] Sintaxe errada. `--key=value`")
        sys.exit(1)
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid argument `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]

if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello Python",
    "pt_BR": "Olá Python",
    "it_IT": "Ciao Python",
    "fr_FR": "Bonjour Python"
}

try:
    print(msg[current_language] * int(arguments["count"])) 
except ValueError:
    print("Please send a number in --count=")
    sys.exit(1)
except KeyError:
    print(f"Please send a valid language, choose from {list(msg.keys())}")
    sys.exit(1)
