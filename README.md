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
**Números inteiros (`int`)**
- Representam números inteiros, positivos ou negativos, sem parte decimal.

**Números de ponto flutuante (`float`)**
- Representam números reais com parte decimal.

    *Operações básicas:* **int e float**
    - Operações aritméticas: `+`, `-`, `*`, `/`, `//`(divisão inteira), `%` (módulo), `**`exponenciação

**Strings (`str`)**
- Representam sequência de caracteres, usadas para armazenar texto.
- Podem ser delimitadas por aspas simples `'` ou aspas duplas `"`.
    
    *Operações básicas:*
    - Concatenação: `+`
    - Repetição: `*`
    - indexação ou fatiamento: `[]`, `[:]`

**Booleanos (`bool`)**
- Representam valores verdadeiro `True` ou falso `False`.
- São úteis em operações lógicas e condicionais.

    *Operações básicas:*
    - Operações lógicas: `and`, `or`, `not`
    - Comparações: `==`, `!=`, `<` , `>`, `<=`, `>=`

**Nulos (`NoneType`)**
- Representam ausência de valor ou um valor nulo.
- É usado para inicializar variáveis ou indicar que uma variável não tem valor atribuído.
    *Operações básicas:*
    - Comparação com `is` ou `is not`

Exemplos:
```
valor = 15 # int

total = 12.4 # float

fruta = "Banana" # string

available = True # bool

nome = None # None
```

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
Para fazer manipulação de arquivos em um programa python é necessário importar a biblioteca *os* usando a instrução `import os`, que vai permitir que sejam feitos comandos de manipulação de arquivos e pastas e efetuar leitura e escrita de arquivos.

## Comandos iniciais para navegação entre pastas e criação de arquivos.
- listar itens em um diretório
```
os.listdir(".")
```
- Criar um diretório

```
os.mkdir("outroDiretorio")
os.makedirs("outroDiretorio", exist_ok=True)
```
- Mudar de diretório
```
os.chdir("outroDiretorio")

```
- Resolvendo problemas de mudança de diretório para SO's distintos.
    - Essa opção é útil, pois o modo de informar a mudança de diretório no Linux se usa a `/`, enquanto no windows é usado o `\`. Para resolver a situação o comando abaixo concatena as pastas e retorna o endereço corretamente para cada um dos SO's.

```
path = os.path.join("diretorio", "diretorioAbaixo")
```
- Criar arquivos
```
os.mknod("arquivo.py")
```
- Criar Arquivos diretamente em um diretório abaixo
```
os.mknod(os.path.join(path, "arquivo.py"))
```

- Retornar o nome do arquivo de um diretório
```
os.path.basename(filepath)
```
## Lendo e escrevendo arquivos
Para manipular arquivos é necessário o *file descriptor* `open`, essa função espera o endereço do arquivo e um argumento que dirá o que o file descriptor fará.

- Como exemplo, foi criada uma variável chamada **filepath** que recebe o endereço de um arquivo chamado `arquivo.txt`.

```
filepath = os.path.join(os.curdir, arquivo.txt)
```

### Escrita de arquivos
Para escrever arquivos é chamado o file descriptor `open`, que recebe o endereço do arquivo e o argumento `"w"`. Há duas formas de serem feitas a escrita em arquivos.
- Forma direta: Nesse modo é passado diretamente a função write, habilitada pelo argumento `"w"`, que recebe o conteúdo que será escrito no arquivo e fecha o file descriptor após escrevê-lo.

```
open(filepath, "w").write("Olá")
```

- Atribuição à variável: Aqui, será criada uma variável que receberá a função `open` e apartir da variável, a função write será chamada.
    - É necessário depois executar a função `close` para fechar o file descriptor.

```
arquivo = open(filepath, "w")
arquivo.write("Olá")
arquivo.close()
```
**Observações**
- Utilizando o argumento `"w"` no file descriptor o conteúdo será *substituído* toda vez que a função `write` for executada, para escrever arquivos de forma incremental, o segundo argumento a ser passado será o `"a"` de append.

- Uma forma mais comum atualmente de se fazer a escrita de arquivo é utilizando o *gerenciador de contextos* `with`. Dessa forma é possível atribuir o file descriptor para uma variável e efetuar a escrita sem a necessidade de fechá-lo.
```
with open(filepath, "a") as arquivo:
    arquivo.write(" Python")
```
- É possível também escrever arquivos a partir de uma lista e escrever em mais de uma linha usando essa lista através da função `writelines`
```
list = ["Olá\n", "Python\n", "Uma linguagem muito interessante\n"]

with open(filepath, "a") as arquivo:
    arquivo.writelines(list)
```

### Leitura de arquivos
Para ler arquivos é chamado o *file descriptor* `open`, que recebe o endereço do arquivo e o argumento `"r"`. Como na escrita, há mais de uma forma de ler arquivos.

- Forma direta: É possível fazer diretamente usando o `print` e dentro passando o *file descriptor* com o endereço do arquivo, o argumento `"r"` e em seguida chamado a função `read()`.
```
print(open(filepath, "r").read("Olá"))
```

- Atribuição à variável: Aqui, será criada uma variável que receberá a o file descriptor open e apartir da variável a função read será chamada.

```
arquivo = open(filepath, "r")
print(arquivo.read("Olá"))
```
**Observações**
- Após a leitura do arquivo, caso tente lê-lo de novo ele retornará em branco, pois a leitura percorreu todo o texto, sendo necessário atribuir a variável o file descriptor novamente.
- Foi feita usando o print para retornar o valor do arquivo em tela, mas em desenvolvimento ou produção, caso não seja necessário imprimir em tela, pode ser feita a leitura do arquivo sem a necessidade da função print. Ex: `arquivo.read("Olá")`
- É possível passar uma lista de itens para um arquivo atraves da função `readlines()`.
```
print(arquivo.readlines())
```

# Tratamento de erros com exceptions

```
try:
    execução a ser feita.
except:
    print(mensagem de erro a ser exibida.)
```

**Configurando exceções para diferentes erros**
Pode haver casos dentro de um bloco try em que um outro erro ocorra e as exceções tem que estar devidamente configuradas para capturar o erro e exibir a mensagem corretamente.

```
try:
    names = open("names.txt").readlines()
    print 1/0
except FileNotFoundError:
    print("Mensagem de erro.")
    sys.exit(1)
except ZeroDivisionError:
    print("Mensagem de erro.")
    sys.exit(1)
```

**Capturando o objeto do erro**
É possível e recomendado capturar o objeto de erro e assim manipular e enviar para o usuário da seguinte forma.

```
try:
    names = open("names.txt").readlines()
    print 1/0
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
```

**Outras expressões**

- else: Será executado sempre que o try for resolvido sem problemas.
- finally: Será executado independente de cair em exceção ou não.

# Logging

```
logging.debug("Mensagem pro dev, QA, sysadmin")
logging.info("Mensagem geral para os usuários")
logging.warning("Aviso que não causa erro.")
logging.error("Erro que afeta uma única execução")
logging.critical("Erro que afeta todo o sistema. Ex: O banco de dados sumiu")
```

É possível ajustar:
- level: por padrão as mensagens de *debug* e *info* não são exibidas, mas forçando a usar o modo de debug, essas mensagens passarão a ser exibidas.

- formatação: É possível ajustar o modo como a mensagem será exibida.

- destino: Assim, pode-se customizar para onde a mensagem de log será exibida.

Para fazer essas alterações é necessário criar uma instância de log própria.
```
log = loggin.Logger("logs.py, logging.DEBUG)
```

# Condicionais
Condicionais são usadas para executar diferentes blocos de código com base em certas condições. São utilizadas as palavras chave `if`, `elif` e `else`.
- O `if` é usado para iniciar um bloco de condição baseado em uma verificação booleana. Se a condição for verdadeira, o bloco interno é executado.
```
n1 = 4
n2 = 6

if n2 > n1:
    print(f"O número {n2} é maior")
```

- O `elif` é chamado caso a condição inicial não seja atendida e exista uma outra condição a ser testada.
```
n1 = 6
n2 = 6

if n2 > n1:
    print(f"O número {n2} é maior.")
elif n2 == 1:
    print("Os números são iguais.")
```

- Por fim o `else` só é invocado caso a(s) condição(ões) não seja(m) atendida(s).
```
n1 = 6
n2 = 3

if n2 > n1:
    print(f"O número {n2} é maior.")
elif n2 == 1:
    print("Os números são iguais.")
else:
    print(f"O número {n2} é menor")
```

## Condicionais ternárias
Quando o objetivo da condição é apenas atribuir valor a uma variável ou imprimir um valor pode-se deixar a condicional `if` mais simples.
```
n1 = 4
n2 = 6

valor = "é maior" if n2 > n1 else "é menor"
```

É possível também operar com condicionais ternárias para atribuir valor através do operador `or` que opera através de *expressões lógicas* onde caso a variável tenha valor falso, usa a opção padrão definida na instrução.

```
nome = "José"
print(f"Olá {nome or "pessoa"}, tudo bem com você?")
```

# Repetições

### While
É a estrutura de repetição usada para executar um bloco de código enquanto uma condição seja verdadeira. Ao contrário do for que iterá sobre uma sequência, o while continua executando enquanto até que a condição se torne falsa.

Estrutura básica
```
n = 0
while n < 5:
    print(n)
    n += 1 # Irá imprimir todos os números de 0 a 4, pois a condição de parada do bloco é n ser menor que 5.
```
- Essa condição que faz o while parar de executar é chamada de *condição de parada*, se isso não for definido, o bloco continuará rodando em um loop infinito, pois não há uma condição onde ela se torne falsa, como no exemplo abaixo.

```
while True:
    print("olá!!") # Esse código rodará em loop infinito.
```
**Palavras-chave**
- `break`: Interrompe o loop.

```
n = 0
while n < 10:
    if i == 5:
        break
    print(i)  # Imprime de 0 a 4
```

- `continue`: Pula a iteração atual e vai para a próxima.
```
n = 0
while n < 10:
    if i % 2 == 0:
        continue
    print(i)  # Irá imprimir apenas os números ímpares de 0 a 9
```

- É possível também que a condição de parada de um loop em while seja um dado recebido de um input.

```
while True:
    entrada = input("Digite um número (ou 'sair' para finalizar): ")
    if entrada.lower() == 'sair':
        break
    if not entrada.isdigit():
        print("Entrada inválida. Tente novamente.")
        continue
    numero = int(entrada)
    print(f"Você digitou o número: {numero}")

```



### For
É a estrutura de repetição usada para iterar sobre uma sequência (strings, listas, tuplas, dicionários e conjuntos) ou qualquer objeto iterável.

Tipos de uso

- Iteração sobre uma lista
```
frutas = ["maça", "banana", "abacaxi"]
for fruta in frutas:
    print(fruta) 
```

- Iteração sobre uma string
```
fruta = "Banana"
for letra in fruta:
    print(letra)
```

- Iteração usando um `range`
    - um `range` gera uma sequencia de números que pode onde a sintaxe básica é (`start`, `stop`, `step`), onde é informado o número com condição para iniciar, outro para parar e um número final opcional para pular a quantidade indicada.
    - O `range` pode também receber apenas um número e representará os números de 0 até o algarismo anterior ao informado.
```
for item in range(10): 
    print(item) # irá imprimir uma sequência de números de 0 a 9.

print item in range(1, 10, 2):
    print(item) # irá imprimir uma sequência de números de 0 a 9 pulando de 2 em 2.
```

**Palavras-chave**
- `break`: Interrompe o loop.

```
for i in range(10):
    if i == 5:
        break
    print(i)  # Imprime de 0 a 4
```

- `continue`: Pula a iteração atual e vai para a próxima.
```
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Irá imprimir apenas os números ímpares de 0 a 9
```
# Funções

**Anatomia de uma função**
- Definição ou atribuição: Atribuição do nome da função antecedido por `def` para sinalizar que é uma função
- Assinatura: Tudo o que estiver entre o nome da função e os `:`
    - Aqui serão informados os parâmentro e anotações de tipo
    - Os parâmetros podem ser posicionais e nomeados.
        - Os posicionais seguem a ordem definida na função, os nomeados é passado o parâmetro atribuindo um valor
        - Os argumentos podem ser passados também empacotando-os, caso os valores estejam em uma tupla. Nesse caso, os valores são passados de forma posicional.
        - Nos casos dos dicionários, eles são passados de forma nomeada
- Documentação: Um pequeno texto descrevendo o que a função faz.
- Valor de retorno: Quando precisar ser retornado mais de um valor, pode ser feito através de uma tupla.

**Sintaxe básica**

```
def soma(x, y ): # assinatura da função
    return x + y # corpo da função
```
- Em python toda função retorna alguma coisa, caso não seja atribuído um retorno, seu retorno será *None*.
    - Funções que não retornam nada são chamadas de procedimentos ou *procedures*.
- Em python, assim como em outras linguagens, é importante seguir o princípio de cada função ter apenas uma responsabilidade.
- Justamente por conta da premissa de cada função ter uma única responsabilidade, usá-las ajuda a manter o código organizado e de fácil leitura.

**Funções Lambda**


### Funções built-in

**Funções em itens iteráveis**
- `sum()`: retorna a soma de todos os valores.
- `max()`: retorna o maior valor.
- `min()`: retorna o menor valor.
- `len()`: retorna a quantidade de valores em uma coleção.
- `reversed()`: retorna a coleção com a ordem inversa da original.
- `sorted()`: Retorna uma lista com todos os itens organizados segundo a tabela ASCII

**Funções voltadas a programação funcional**
- `filter()`: 
- `map()`:
- `all()`:
- `enumerate()`:
- `zip()`:

### Funções da biblioteca padrão do Python

- random
    - `random.random()`: Retorna um número entre 0.0 e 1.0
    - `random.randint(ini, fim)`: Retorna um número inteiro entre o range passado como argumento.
    - `random.choice(colecao)`: Retorna um item aleatório dentro de dentro de uma coleção.
    - `random.sample(colecao, items)`: Retorna a quantidade de items informada de dentro de uma coleção.
    - `random.shuffle(colecao)`: Embaralha uma coleção inclusive alterando a variável passada

- itertools
    - `itertools.cycle()`:
    - `itertools.repeat()`:
    - `itertools.accumulate()`:
    - `itertools.product()`:
    - `itertools.permutation()`:
    - `itertools.combinations()`:

- functools
    - `functools.partial()`

- statistics
    - `statistics.mean()`: Calcula a média em uma coleção de valores
    - `statistics.median()`: Calcula a mediana em uma coleção de valores

- getpass
    - `getpass.getpass()`: Usado para ser um input para senhas, essa função oculta o que está sendo digitado.
    teste