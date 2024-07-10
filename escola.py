#!/usr/bin/env python3

"""
Exibir relatório de crianças por atividade.

- Imprimir uma lista de crianças agrupadas por sala que frequentam cada uma das atividades.
"""

__version__ = "0.2.0"

sala1 = ["Erick", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isabela"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Isabela", "João"]

atividades = [("Inglês", aula_ingles), ("Música", aula_musica), ("Dança", aula_danca)]


for nomeAtividade, atividade in atividades:
    atividadesSala1 = set(atividade) & set(sala1)
    atividadesSala2 = set(atividade) & set(sala2)

    print("{:#^50}".format(f" Aula de {nomeAtividade} "))
    print("{:#^50}".format(" Sala 1 "))
    for aluno in atividadesSala1:
        print(aluno)

    print("{:#^50}".format(" Sala 2 "))
    for aluno in atividadesSala2:
        print(aluno)
    print()