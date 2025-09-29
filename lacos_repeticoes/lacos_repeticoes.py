# percorre a lista de nomes e exiba cada um

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

# loop

contador = 0

while contador < 11:
    print(f'Contador atual: {contador}')
    contador += 1

# exiba a mensagem 5 vezes

for i in range(5):
    print("Bem-vindo ao Buscante!")

# programa para implementar a soma

valores = [10, 20, 30, 40, 50]

soma = 0
for valor in valores:
    soma += valor

print(f"A soma total das receitas é: {soma}")

# percorre a lista de projetos e exibe os nomes dos projetos válidos

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print('Projeto ausente')
    else:
        print(projeto)

# encontrar item 
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == 'O Hobbit':
        print(f'Livro encontrado: {livro}')
        break

# imule as vendas de um livro com o estoque inicial de 5 exemplares

estoque = 5

while estoque > 0:
    estoque -= 1
    print(f"Venda realizada! Estoque restante: {estoque}")
print('Estoque esgotado')

# contagem regressiva

segundos = 10
for segundos in range(10,0,-1): #10 é o início, 0 é o limite final (mas ele não é incluído), -1 indica que a contagem é decrescente
    if segundos % 2 == 0:
        print(f'Faltam apenas {segundos} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {segundos} segundos restantes.')
print('Aproveite a promoção agora!')

#  programa que exibe somente os livros que possuem estoque disponível

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro['estoque'] == 0:
        continue
    print(f'Livro disponível: {livro['nome']}')

# cadastro com minimo de caracteres

while True:
    nome = input('Digite seu nome de usuário: ')
    senha = int(input('Digite sua senha: '))

    if len(nome) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres')
        continue

    if len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteres')
        continue

    
    print('Cadastro realizado com sucesso!')
    break