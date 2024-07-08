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
