#EXERCICIO 1

    # '''1. Faça um programa para exibir os números de 1 a 100.'''
# x=1
# while x <= 100:
#     print(x)
#     x+=1

#EXERCICIO 2

    # '''2. Faça um programa para exibir os números de 50 a 100.'''
# x=50
# while x <= 100:
#     print(x)
#     x+=1

#EXERCICIO 3

    # '''3. Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! Na tela.'''

'''Para termos um delay na exibição dos números chamamos a função Sleep da biblioteca Time dessa forma:
from BIBLIOTECA import FUNÇÃO'''
# from time import sleep
# print("Esse programa exibe a contagem regressiva de um foguete.\n")
# n=10
# while n >= 0:
#    print(n)
#    n-=1
#    sleep(1)
'''Usar assim: sleep(segundo)'''
# print("\nFogo!!!")

#EXERCICIO 4
    #4. Faça um programa para imprimir de 1 até o número
    # digitado pelo usuário que mostre apenas os números
    # ímpares.

# print("Esse programa exibe os números ímpares até o número que voce digitar.")
#
# fim = int(input("Digite um número: "))
# x = 1
# while x <= fim:
#     if x/2 != 0:
#         print(x)
#         x += 2

#EXERCICIO 5
    #5. Faça um programa para escrever os 10 primeiros
    #múltiplos de 3.

# print("Esse programa exibe os 10 primeiros múltiplos de 3")
# x=0
# while x <= 10:
#     x+=3
#     print(x)

#EXERCICIO 6
    #6. Faça um programa para exibir os resultados de uma
    #tabuada no formato: 2 x 1 = 2, 2 x 2 = 4, ...

# x=1
# n = int(input("Tabuada do: "))
# while x<=10:
#     print(n, " X ", x, " = ", n*x)
#     x+=1

#EXERCICIO 7
    #Modifique o programa interior de forma que o usuário
    # também digite o início e o fim da tabuada, em vez de
    # começar com 1 e 10.

# print("Esse programa cria uma tabuada personalizada.\n")
# x = int(input("Número do primeiro múltiplicador: "))
# y = int(input("Número do último múltiplicador: "))
# n = int(input("Múltiplicador padrão: "))
# while x<=y:
#     print(n, " X ", x, " = ", n*x)
#     x+=1

