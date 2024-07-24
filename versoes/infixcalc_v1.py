#! /usr/bin/env python3

"""Funcionamento

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso: 
$ infixcalc.py sum 5 2
> 7

O histórico de operações deverá ser salvo em `infixcalc.log`
"""

__version__ = "0.1.1"

import os
import sys
import operator
from datetime import datetime

operations = {
    "sum": operator.add,
    "sub": operator.sub,
    "mul": operator.mul,
    "div": operator.truediv
}

arguments = sys.argv[1:]

if not arguments:
    operator = input("Informe a operação: sum/sub/mul/div: ")
    n1 = input("Informe um número: ")
    n2 = input("Informe outro número: ")
    arguments = [operator, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos.")
    print("Exemplo: `sum 1 1`")
    sys.exit(1)
    
operator, *nums = arguments

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Valor inválido: {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

try:
    functional_operator = operations[operator]
except KeyError:
    print("Please send a valid operation `sum/sub/mul/div`")
    sys.exit(1)

total = functional_operator(n1, n2)


path = os.curdir
filepath = os.path.join(path, "infixcalc.log")

with open(filepath, "a") as log:
    log.write(f"{n1} {operator} {n2} = {total} {datetime.now().isoformat()},\n")

print(total)