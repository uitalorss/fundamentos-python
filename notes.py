#! /usr/bin/env python3

"""Bloco de notas via terminal

$ notes.py new "Título"
tag: tech
text: descrição da nota.

$ notes.py read --tag=tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

arguments = sys.argv[1:]

commands = ("read", "new")

filepath = os.path.join(os.curdir, "notes.txt")

if not arguments:
    print("Favor passar algum comando.")
    sys.exit(1)

if arguments[0] not in commands:
    print("Favor passar argumentos válidos.")
    sys.exit(1)

if arguments[0] == "new":
    titulo = arguments[1]
    note = [
        f"{titulo}",
        input("Tag: ").strip(),
        input("Text: ").strip()
    ]

    with open(filepath, "a") as notelist:
        notelist.write("\t".join(note) + "\n")
    print("Nota salva com sucesso.")

if arguments[0] == "read":
    for line in open(filepath):
        titulo, tag, texto = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Titulo: {titulo}")
            print(f"Tag: {tag}")
            print(f"texto: {texto}")
            print("-" * 50)