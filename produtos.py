#!/usr/bin/env python3

"""Cadastro de produtos"""
__version__ = "0.1.0"

produto = {
    "nome": "Caneta",
    "cor": ["azul, branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8
    },
    "estoque": True,
    "codigo": "45678",
    "codebar": None
}

total = produto["preco"] * 3
print(f"O cliente comprou {produto['nome']} e pagou um total de R$ {total}")