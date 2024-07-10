# fundamentos-python

#Configuração de ambiente virtual
```
python3 -m venv .venv
source .venv/bin/activate

```

#Atualização do gerenciador de pacotes pip e instalação de pacotes

```
python3 -m pip install --upgrade pip

python3 -m pip install nomeDoPacote
```

# Tipos de dados

### Simples
### Compostos
**Tupla**
- Forma de atribuição: ```cores = red, green, blue``` ou ```cores = (red, green, blue)```
    > Há casos em que a atribuição de uma tupla é obrigatória envolver entre parênteses, como na interpolação de strings.
- Uma tupla é **imutável**, ou seja, uma vez atribuída, não é possível adicionar, remover ou alterar os dados dentro da tupla.
- Quando necessário acessar o item em uma tupla, basta passar a sua posição entre colchetes. Exemplo: ```print(cores[0])```
- O método de desempacotar uma tupla é interessante para tirar valores de uma lista e atribuir a variáveis.
```
pontos = 4, 1, 50
x, y, z = pontos

print(x)
> 4
print(y)
> 1
print(z)
> 50
```

**Lista**
- Bastante similar aos arrays de outras linguagens de programação.
- Diferente das tuplas, as listas são **mutáveis**. Sendo assim permitidas a manipulação dos itens da lista.
- Comporta itens de qualquer tipo.
```
users = []
colors = ["red", "green"]
```
**Set**
- É um tipo de dado que recebem elementos **iteráveis**, como tuplas e listas.
- O set cria uma lista *não ordenada* de elementos **únicos**, não permitindo repetições.
    - A melhor usabilidade do set é voltado a pegar um dado iterável e remover as duplicatas existentes.
- Pode ser criado vazio e ir adicionando elementos.

- Forma de criação
```
conjunto = {1, 2, 3} ou conjunto = set(1, 2, 3) - A segunda opção é mais recomendada.
```
- Operações
    - União: Essa operação une dois ou mais conjuntos, eliminando as repetições.
    ```
    conjunto_a = set((1, 2, 3, 4, 5))
    conjunto_b = set((4, 5, 6, 7, 8))
    print(conjunto_a|conjunto_b)
    > {1, 2, 3, 4, 5, 6, 7, 8}
    ```
    - Interseção: A operação retorna um set com os dados que estão em todos os conjuntos envolvidos na operação.
    ```
    print(conjunto_a & conjunto_b)
    > {4, 5}
    ```

    - Diferença: A operação retorna um set com os dados que não estão em um conjunto em relação a outro.
        - Nessa operação a ordem importa, pois os resultados de um set para outro serão diferentes.
    ```
    print(conjunto_a - conjunto_b)
    > {1, 2, 3}

    print(conjunto_b - conjunto_a)
    > {6, 7, 8}
    ```

    - Diferença simétrica: A operação que é o oposto da interseção, retornando um set com os dados que não são presentes nos dois sets.
    ```
    print(conjunto_a ^ conjunto_b)
    > {1, 2, 3, 6, 7, 8}
    ```
**Dicionário**


# Modelos de formatação
- Concatenação

```print("Uítalo " + "Souza")```

- Interpolação

```print("O saldo de %s é de R$ %.2f" % ("Uítalo", 2000))```

- str.format
```
msg = "Olá {:s}, portador do id {:03d}, seu saldo total é de {:.3f}"

print(msg.format("Uítalo", 43, 605))
```
- f-strings
```
nome = "José"
status = "inativo"

print(f"Bem-vindo, {nome}, seu status atual é {status}.")
```
