# alunos = ["g", "n", "l", "v"]
# for i in alunos:
#     print(i)

# alunos = ["goat", "rugal", "goão", "D2"]
# nome = input("Entre com o nome do estudante para pesquisar: ").capitalize()
# for i in alunos:
#     if i == nome:
#         print("Aluno encontrado!")
#         break
#     else:
#         print("Aluno não encontrado!")

# for i in range(1,11):
#     if i %2 == 0:
#         print(i)

# num = 0
# for i in range(0,21,2):
#     print("2 x ",num," = ",i)
#     num += 1

# L = [1, 7, 2, 4]
# maximo = L[0]
# for e in L:
#     if e > maximo:
#         maximo = e
# print(maximo)

# L = [1, 7, 2, 4]
# print(max(L))

    #1. Altere o programa do exemplo anterior de formar a imprimir o menor elemento da lista.

# L = [1, 7, 2, 4]
# menor = L[0]
# for e in L:
#     if e < menor:
#         menor = e
# print(menor)

    #2. A lista de temperaturas de Mons, na Bélgica, foi
# armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça
# um programa que imprima a menor e a maior
# temperatura, assim como a temperatura média.

# T = [-10, -8, 0, 1, 2, 5, -2, -4]
# maior = T[0]
# menor = T[0]
# for x in T:
#     if x < menor:
#         menor = x
#     if x > maior:
#         maior = x
# print("A menor temperatura foi ",menor," e a maoir foi ", maior)

    #3. Faça um programa para selecionar os elementos de
# uma lista e copiá-los para outras. Copiar os valores
# pares para a lista P que estão na lista V = [9, 8, 7, 12, 0,
# 13, 21] e os ímpares para a lista I.


# V = [9, 8, 7, 12, 0, 13, 21]
# I = []
# P = []
# for x in V:
#    if x % 2 == 0:
#         P.append(x)
#    else:
#        I.append(x)
# print("Números Pares: ", P)
# print("Números Impares: ", I)

    #4. Faça um programa que lê e imprime uma lista de
#compras até que seja digitado fim.

lista = ["maça", "banana", "pera", "melão", "melancia"]
while True:
    item = input("Adicione um item a lista de compra. Quando finalizar digite fim: ")
    if item == "fim":
        print("A lista está encerrada.")
        break
    lista.append(item)
    for x in lista:
        print(x)