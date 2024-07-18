#! /usr/bin/env python3

"""
Haverá um template de mensagem e será exibido no terminal a mensagem iterando por uma lista de clientes.
"""

__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]

# TODO: Verificar os nomes dos arquivos se estão sendo passados corretamente.

if not arguments:
    print("Informe o nome do arquivo de emails esperado")
    sys.exit(1)

path = os.curdir
filepath_email = os.path.join(path, arguments[0])
filepath_template = os.path.join(path, arguments[1])

for line in open(filepath_email):
    nome, email = line.split(",")
    print(
        open(filepath_template).read() 
        % {
            "email": email,
            "nome": nome,
            "produto": "Caneca",
            "link": "http://www.canecas.com.br",
            "quantidade": 12,
            "preco": 19.9
        }
    )