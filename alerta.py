#! /usr/bin/env python3

"""
Alerta de temperatura

Faça um script que pergunte ao usuário qual a temperatura atual e o índice de umidade do ar sendo que para cada caso será exibida uma mensagem de alerta dependendo das condições.

Temperatura maior que 45: ALERTA!!! Perigo Calor extremo.
Temperatura 3 vezes maior ou igual que a umidade: ALERTA!!! Perigo calor úmido.
Temperatura entre 30 e 40: Muito calor
Temperatura entre 10 e 30: Normal.
Temperatura entre 0 e 10: Frio.
Temperatura abaixo de 0: ALERTA!! Perigo frio extremo.
"""

import sys
import logging
__version__ = "0.1.2"
__author__ = "Uítalo Souza"

log = logging.Logger("Alerta")

info = {
    "temperatura": None,
    "umidade": None
}

def is_completely_filled(dict_inputs):
    info_size = len(dict_inputs)
    filled_size = 0
    for item in dict_inputs.values():
        if item is not None:
            filled_size += 1
    return filled_size == info_size

def read_inputs(dict_info):
    for key in dict_info.keys():
        if dict_info[key] is not None:
            continue
        try:
            dict_info[key] = float(input(f"Informe a {key} atual: ").strip())
        except ValueError:
            log.error(f"Erro!! {key.capitalize()} inválida!")
            break

while not is_completely_filled(info):
    read_inputs(info)
    

temperatura = info["temperatura"]
umidade = info["umidade"]

if temperatura > 45:
    print("ALERTA!!! Perigo calor extremo.")
elif temperatura * 3 >= umidade:
    print("ALERTA!!! Perigo Calor úmido.")
elif temperatura >= 30 and temperatura <= 45:
    print("ALERTA!!! Muito calor.")
elif temperatura >= 10 and temperatura < 30:
    print("Normal")
elif temperatura >= 0 and temperatura < 10:
    print("Frio")
else:
    print("ALERTA!! Perigo frio extremo.")