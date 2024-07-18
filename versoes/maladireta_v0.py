#! /usr/bin/env python3

"""
Haverá um template de mensagem e será exibido no terminal a mensagem iterando por uma lista de clientes.
"""

__version__ = "0.1.0"


email_template = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s ?

Clique agora em %(link)s

Apenas %(quantidade)d unidades disponíveis.

preço promocional: R$ %(preco).2f
"""

clientes = ["Maria", "João", "José"]

for cliente in clientes:
    print(
        email_template % {
            "nome": cliente,
            "produto": "Caneca",
            "link": "http://www.canecas.com.br",
            "quantidade": 12,
            "preco": 19.9
        }
    )