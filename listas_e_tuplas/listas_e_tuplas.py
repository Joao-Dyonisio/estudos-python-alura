#Verficação o item na lista

# lista = ['açucar', 'sal', 'café']
# item_desejado = input('Digite o item que você quer verificar: ')

# if item_desejado in lista:
#     print(f'O {item_desejado} está na lista')
# else:
#     print(f'Esse item não está na lista')

# 2) desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

# notas = [85, 70, 90, 60, 75]
# notas.sort()
# print("Notas ordenadas:", notas)

# 3) criar um programa que permita registrar os voluntários e exiba a lista completa no final.

# voluntarios = []

# while True:
#     nome_do_voluntario = input("Digite o nome do voluntario (ou 'sair' para encerrar): ")
#     if nome_do_voluntario.lower() == "sair":
#         break
#     else:
#         voluntarios.append(nome_do_voluntario)
# print("\n Voluntários na lista: ", voluntarios)

#4) Um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?

# produtos_do_estoque_1 = input("Digite os produtos do estoque 1 (separados por vírgula): ").split(", ")
# produtos_do_estoque_2 = input("Digite os produtos do estoque 2 (separados por vírgula): ").split(", ")

# estoque = produtos_do_estoque_1 + produtos_do_estoque_2
# print("\n Estoque combinado: ", estoque)

# 5) criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?

# lista_convidados = ['Ana', 'Pedro', 'Carlos']
# print(f"Lista atual de convidados: {lista_convidados}")

# novo_convidado = input("Digite o nome do novo convidado: ")
# posicao_da_lista = int(input("Digite a posição na qual deseja inserir o convidado: "))

# lista_convidados.insert(posicao_da_lista -1, novo_convidado)
# print(f"Lista atualizada de convidados: {lista_convidados}")

# 6) crie um programa que permita ao organizador ordená-los, de forma que a lista final siga a sequência correta.

# eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
# print(eventos_registrados)
# eventos_registrados.sort()
# print(eventos_registrados)

# 7) Um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final

nomes = ["Ana", "Carlos", "Pedro"]
print("Lista original:", nomes)