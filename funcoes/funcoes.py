# calcular idade

def calculo_idade(nascimento, atual):
    return atual - nascimento


ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = calculo_idade(ano_nascimento, ano_atual)

print(f'A idade é {idade}')


# função que receba uma palavra e exiba a quantidade de caracteres

def tamanho_palavra(palavra):
    return len(palavra)

palavra_escolhida = input('Digite uma palavra: ')
print(f'Essa palavra tem {tamanho_palavra(palavra_escolhida)} caracteres')

# saudação personalizada dependendo da hora

def saudacao(horario):
    if horario < 12:
        return "Bom dia"
    elif horario < 18:
        return "Boa tarde"
    else:
        return "Boa noite"
    
horario_atual = int(input('Digite a hora atual (0-23): '))
print(saudacao(horario_atual))

# converte os tipos para inteiro e verifica se a conversão foi feita corretamente

def conversao(lista):
    return [int(telefone) for telefone in lista]

def verificar(lista):
    for num in lista:
        if not isinstance(num, int):
            return "Erro na conversão."
    return 'Todos os números foram convertidos corretamente!'
   
telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = conversao(telefones)
print(verificar(telefones_convertidos))

# converta os valores para números e exiba o total

valores = input('Digite os valores das vendas:').split()
total = sum(map(float, valores)) # map(função,iterável)
print(f'O total de vendas foi: {total}')


#  lista de números que exiba apenas os pares

numero = input('Digite os números separados por espaço: ').split()
pares = filter(lambda x: int(x) % 2 == 0, numero )
print(f'Números pares: {" ".join(pares)}')

#  junte as listas e exiba o resultado no formato produto: preço

produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}") 

# programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

soma = lambda x, y: x + y 

subtrai = lambda x, y: x - y 

multiplica = lambda x, y: x * y 

divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero" 

x = float(input("Digite o primeiro número: ")) 

y = float(input("Digite o segundo número: ")) 

operacao = input("Escolha a operação (| + | - | * | / |): ") 

operacoes = { 

    '+': soma,  

   '-': subtrai, 

    '*': multiplica, 

    '/': divide 

} 

if operacao in operacoes:  

   resultado = operacoes[operacao](x, y)  

   print(f"O resultado é: {resultado}")  

else:  

   print("Operação inválida") 

# calcular o preço final com um desconto definido pelo usuário.

def desconto(porcentagem):
   def desconto_aplicado(valor_compra):
      return valor_compra - (valor_compra * (porcentagem/100))
   return desconto_aplicado

desconto_digitado = float(input('Digite a porcentagem de desconto: '))
calcular_preco_final = desconto(desconto_digitado)

valor = float(input('Digite o valor da compra: '))

print(f'Preço final com desconto: {calcular_preco_final(valor)}')

#  soma de todos os números inteiros de 1 até N.

def soma_recursiva(n): 
    if n == 1: 
        return 1 
    return n + soma_recursiva(n - 1) 
 
numero = int(input("Digite um número: ")) 
print(f"A soma de 1 a {numero} é: {soma_recursiva(numero)}") 