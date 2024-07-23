#!/usr/bin/env python3

"""Exemplos de funções"""

# Function
from math import sqrt
def soma(x, y):
    return x + y

valor = soma(2, 3)
print(valor)

# Procedure
def print_upper(text):
    print(text.upper())

print_upper("uítalo")

def calculo_triangulo(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return sqrt(area)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37)
]

print(calculo_triangulo(3, 4, 5))

for t in triangulos:
    area = calculo_triangulo(t[0], t[1], t[2])
    print(f"A área do triangulo é {area}")