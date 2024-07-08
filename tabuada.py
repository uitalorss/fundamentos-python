#! /usr/bin/env python3

"""
Exibindo a tabuada de 1 até 10.
"""

__version__ = "0.1"
__author__ = "Uítalo"

numeros = list(range(1, 11))

for multiplicando in numeros:
    print("{:-^25}".format(f" Tabuada do {multiplicando} "))
    for multiplicador in numeros:
        resultado = multiplicando * multiplicador
        print("{:^25}".format(f"{multiplicando} * {multiplicador} = {resultado}"))
    print("#" * 25)