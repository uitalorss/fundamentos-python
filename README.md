# fundamentos-python

### Configuração de ambiente virtual
```
python3 -m venv .venv
source .venv/bin/activate

```

### Atualização do gerenciador de pacotes pip e instalação de pacotes

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
    
- É um tipo de dado iterável que armazena conjuntos de dados tipo chave e valor.
    - É possível armazenar praticamente qualquer tipo de dado como valor, inclusive outro dicionário.
- É mutável.
- Assim como o *set*, ele não permite chaves duplicadas.

- Forma de criação
    
```
pessoa = {
    "nome": "João"
    "sobrenome": "Da Silva"
    "idade": 28
    "filhos": False
}
```

- Retornando dados de um dicionário

```
print(pessoa["nome"])
```

- Adicionando itens no dicionário

```
pessoa["cidade natal"] = Salvador
pessoa["nome"] = João José // Nesse caso ele irá acessar o dicionário e alterar a chave correspondente, já que ele já existe.
```

- excluir itens no dicionário
```
del pessoa["cidade natal"]
```

- Retornar dados como tuplas
```
print(pessoa.items())
> ([("nome", "João José"), ("sobrenome", "Da Silva"), ("idade", 28), ("filhos", False)])
```    



# Modelos de formatação
**Concatenação**

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
# Manipulando arquivos e pastas

```
import os
# listar itens em um diretório
os.listdir(".")

    # Para resolver possíveis problemas de compatibilidade, pode substituir o "." por os.curdir
    os.listdir(os.curdir)

# Criar diretório
os.mkdir("outroDiretorio")
os.makedirs("outroDiretorio", exist_ok=True)

# mudar de diretório
os.chdir("outroDiretorio")

# Resolvendo problemas de mudança de diretório para SO's distintos.
path = os.path.join("diretorio", "diretorioAbaixo")

# Criar arquivos
os.mknod("arquivo.py")

    # Criar Arquivos diretamente em pastas abaixo
    os.mknod(os.path.join(path, "arquivo.py"))


# Retornar o nome do arquivo de um diretório
os.path.basename(filepath)
```

**Lendo e escrevendo arquivos**
```
filepath = os.path.join(os.curdir, arquivo.txt)

# Para manipular arquivos é necessário o file descriptor open, essa função espera o nome do arquivo e um argumento que dirá o que o file descriptor fará.

# Escrever arquivos
    Para escrever arquivos é chamado o file descriptor open, que recebe o endereço do arquivo e o argumento "w".
    # Forma direta.
        # Nesse modo é passado diretamente a função write, habilitada pelo argumento "w", que recebe o conteúdo que será escrito no arquivo e fecha o file descriptor após escrever o arquivo.
        
        open(filepath, "w").write("Olá")

    # Atribuindo a variável
        # Aqui, será criada uma variável que receberá a função open e apartir da variável, a função write será chamada.
        # É necessário depois executar a função close para fechar o file descriptor.
        
        arquivo = open(filepath, "w")
        arquivo.write("Olá")
        arquivo.close()

    ! Após escrever em um arquivo, caso deseje escrevê-lo novamente, o conteúdo será substituído.
    ! Para escrever arquivos de forma incremental, o segundo argumento a ser passado será o "a" de append.

        # Para não ser necessário a chamada da função close, é necessário criar esse processo dentro do gerenciado de contexto with.
        # Essa é a forma comumente usada para escrita de arquivos.
        with open(filepath, "a") as arquivo:
            arquivo.write(" Python")

    # Escrever arquivos a partir de uma lista
    # É possível passar uma lista de itens para um arquivo atraves da função writelines.
    list = ["Olá\n", "Python\n", "Uma linguagem muito interessante\n"]

    with open(filepath, "a") as arquivo:
        arquivo.writelines(list)

# Ler arquivos
    # Para escrever arquivos é chamado o file descriptor open, que recebe o endereço do arquivo e o argumento "r".
    
    # Forma direta.
        # É possível fazer diretamente usando o print e dentro passando o file descriptor com o endereço do arquivo, o argumento "r" e em seguida chamado a função read().
        
        print(open(filepath, "r").read("Olá"))

    # Atribuindo a variável
        # Aqui, será criada uma variável que receberá a o file descriptor open e apartir da variável a função read será chamada.
        
        arquivo = open(filepath, "r")
        print(arquivo.read("Olá"))
    
    ! Após a leitura do arquivo, caso tente lê-lo de novo ele retornará em branco, pois a leitura percorreu todo o texto, sendo necessário atribuir a variável o file descriptor novamente.
    ! Foi feita usando o print para retornar o valor do arquivo em tela, mas em desenvolvimento ou produção, caso não seja necessário imprimir em tela, pode ser feita a leitura do arquivo sem a necessidade da função print.

    arquivo.read("Olá")

    # Ler arquivos como uma lista
    # É possível passar uma lista de itens para um arquivo atraves da função readlines.

    print(arquivo.readlines())
 ```