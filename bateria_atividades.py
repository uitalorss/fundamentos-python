#! /usr/bin/env python3

import sys
import os

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

bedroom_file = "quartos.txt"
booking_file = "reserva.txt"
bedrooms = {}
bookings = {}

try:
    for line in open(booking_file):
        customer,book,days = line.strip().split(",")
        bookings[int(book)] = {
            "customer": customer,
            "days": days 
        }
except FileNotFoundError:
    print("Arquivo não encontrado")
    sys.exit(1)

try:
    for line in open(bedroom_file):
        num, description, price = line.strip().split(",")
        bedrooms[int(num)] = {
            "description": description,
            "price": float(price),
            "available": False if int(num) in bookings else True
        }
except FileNotFoundError:
    print("Arquivo não encontrado")
    sys.exit(1)

print("Hotel Pythonico")
print("")
print("Quartos disponíveis")
print("*" * 50)
if len(bookings) == len(bedrooms):
    print("Todos os quartos estão ocupados.")
    sys.exit(0)
else:
    for codigo, dados in bedrooms.items():
        description = dados["description"]
        price = dados["price"]
        available = dados["available"]
        if dados["available"] == True:
            print(f"{codigo} - {description} - {price}\n")
    print("")

while True:
    bedroom_to_reserve = int(input("Informe o número do quarto: "))
    if bedroom_to_reserve not in bedrooms or not str(bedroom_to_reserve).isdigit():
        print("Número de quarto inválido.")
    elif bedrooms[bedroom_to_reserve]["available"] == False:
        print("Quarto já reservado.")
    else:
        break

while True:
    amount_days = input("Informe a quantidade de dias de estadia: ")
    if not amount_days.isdigit():
        print("Número de dias de estadia inválido.")
    elif not int(amount_days) < 1 and int(amount_days) >= 20:
        print("Informe uma quantidade de dias válida")
    else:
        break

total = int(amount_days) * bedrooms[bedroom_to_reserve]["price"]
bedroom_chosen = bedrooms[bedroom_to_reserve]["description"]

print("")

print(f"Quarto escolhido: {bedroom_chosen}\nTotal a pagar: R$ {total}")


while True:
    customer_name = input("Nome completo: ").strip()
    if customer_name != "":
        break
    else:
        print("Favor informar um nome válido.")

try:
    with open(booking_file, "a") as booking:
        booking.write(f"{customer_name},{bedroom_to_reserve},{amount_days}\n")
        print("Reserva Efetuada com sucesso.")
except:
    print("Reserva não efetuada.")
    sys.exit(1)