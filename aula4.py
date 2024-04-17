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

# EXEMPLO:

    # Vejamos um programa para corrigir um teste de múltipla
    # escolha com três questões. A resposta da 1ª é “b”, da 2ª é “a”
    # e da 3ª é “d”. O programa conta com 1 ponto a cada resposta
    # correta.

# print("Esse programa é um gabarito de uma prova.\n")
# pontos = 0
# questao = 1
# while questao <= 3:
#     resposta = input(f"Me fale a resposta da questão {questao}: ")
#     if questao == 1 and resposta == "b":
#         pontos = pontos + 1
#     elif questao == 2 and resposta == "a":
#         pontos = pontos + 1
#     elif questao == 3 and resposta == "d":
#         pontos = pontos + 1
#     questao = questao + 1
# print(f"O aluno fez {pontos} ponto(s).")

# EXEMPLO ACUMULADOR

    # Em programas para calcular o total de uma soma, por
    # exemplo, precisamos de acumuladores. A diferença entre um
    # contador e um acumulador é que nos contadores o valor
    # adicionado é constante e nos acumuladores, variável.
    # Vejamos um programa que calcule a soma de 10 números.

# print("Esse programa exemplifica o uso do acumulador através de uma soma.\n")
# cont = 0
# acumulador = 0
# while cont < 10:
#     cont+=1
#     x = float(input(f"Digite o {cont}º número a ser somado: "))
#     acumulador += x
# print(f"A soma é igua a {acumulador:.2f}")
# print(f"A media é igua a {acumulador/cont:.2f}")

# EXERCICIO 8

    # 8. Escreva um programa que pergunte o depósito inicial
    # e a taxa de juros de uma poupança. Exiba os valores
    # mês a mês para os 24 primeiros meses. Escreva o total
    # do ganho com juros no período.

# print("Esse programa calcula o valor de juros de um depósito mês a mês durante 24 meses.\n")
# deposito = float(input("Digite deposito inicial: "))
# juros = int(input("Digite a taxa de juros  a ser acrecida em cada mês: \n"))
# mes = 0
# while mes < 24:
#     mes += 1
#     print(f"No {mes}º mês o valor total contando com a taxa será de {deposito:.2f}")
#     deposito = deposito + deposito * (juros/100)
# print(f"\nO valor total ao final do investimento de {deposito:.2f}.")

# EXERCICIO 9

    # Altere o programa anterior de forma a perguntar
    # também o valor depositado mensalmente. Esse valor
    # será depositado no início de cada mês e você deve
    # considerá-lo para o cálculo de juros do mês seguinte.

# print("Esse programa calcula o valor de juros de um depósito mês a mês durante 24 meses. Voce poderá depositar mensalmente também.\n")
# deposito = float(input("Digite deposito inicial: "))
# juros = int(input("Digite a taxa de juros  a ser acrecida em cada mês: \n"))
# mes = 0
# while mes < 24:
#     mes += 1
#     print(f"No {mes}º mês o valor total contando com a taxa será de {deposito:.2f}")
#     dmensal = float(input(f"Digite o seu deposito no {mes}º mês."))
#     deposito = dmensal + deposito + deposito * (juros/100)
# print(f"\nO valor total ao final do investimento de {deposito:.2f}.")
