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
