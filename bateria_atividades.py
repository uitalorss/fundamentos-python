#! /usr/bin/env python3

import sys

"""
Faça um programa que imprima os números pares de 1 a 200

n = 1
for n in range(1, 201):
    if n % 2 == 0:
        print(n)
"""

"""
Alerta de temperatura

Faça um script que pergunte ao usuário qual a temperatura atual e o índice de umidade do ar sendo que para cada caso será exibida uma mensagem de alerta dependendo das condições.

Temperatura maior que 45: ALERTA!!! Perigo Calor extremo.
Temperatura 3 vezes maior ou igual que a umidade: ALERTA!!! Perigo calor úmido.
Temperatura entre 30 e 40: Muito calor
Temperatura entre 10 e 30: Normal.
Temperatura entre 0 e 10: Frio.
Temperatura abaixo de 0: ALERTA!! Perigo frio extremo.

import logging

log = logging.Logger("Alerta")

info = {
    "temperatura": None,
    "umidade": None
}

for key in info.keys():
    try:
        info[key] = float(input(f"Informe a {key} atual: ").strip())
    except ValueError:
        log.error(f"Erro!! {key.capitalize()} inválida!")
        sys.exit(1)

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
"""

"""
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprima de volta o que foi digitado com as vogais duplicadas.

Ex:
'Digite uma palavra (ou aperte enter para sair): Python'
'Digite uma palavra (ou aperte enter para sair): Bruno'
Pythoon
Bruunoo

vogais = ["a", "e", "i", "o", "u"]
listaPalavras = []

while True:
    palavra = input("Digite uma palavra (ou enter para sair): ").strip()
    if not palavra:
        break
    novaPalavra = ""

    for letra in palavra:
        novaPalavra += letra
        if letra.lower() in "aãáâeêéiíoõôóuú":
            novaPalavra += letra
    listaPalavras.append(novaPalavra)

print(*listaPalavras, sep="\n")
"""

"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos disponíveis para alugar e o preço de cada quarto, esta informação está disponível em um arquivo de texto separado por vírgulas.

`quartos.txt`
1,Suite Master,500
2,Quarto Família,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário qual o número do quarto a ser reservado e a quantidade de dias e no final exibe o valor estimado a ser pago.
O programa deve salvar esta escolha em outro arquivo contendo as reservas.

`reservas.txt`
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deverá exibir uma mensagem informando que já está reservado.

"""
