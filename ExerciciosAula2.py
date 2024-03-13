    # Exercicio 4

# print("Esse programa solicita dois números inteiros e faz a sua soma")
# n1 = int(input("Coloque o primeiro número "))
# n2 = int(input("Coloque o segundo número "))
# print("A soma dos dois números é ", n1+n2)

    # Exercicio 5

# print("Esse programa converte números em metros para milimetros.")
# m = float(input("Escreva o número em metros: "))
# mm = m*1000
# print(f"O número convertido é igual a {mm:.2f}.")

    # Exercicio 6

# print("Esse programa converte o periodo de dias, hora, minutos e segundos no total de segundos:")
# dias = int(input("Diga-me a quantidade de dias: "))
# horas = int(input("Agora, diga-me as horas: "))
# minutos = int(input("Estamos quase lá, diga-me os minutos: "))
# segundos = int(input("Por fim, diga-me os segundos: "))
# tsegundos = (minutos*60)+(horas*3600)+(dias*86400)+segundos
# print("A quantidade de", dias,"dias,", horas, "horas e ", minutos, "minutos é igual a", tsegundos, "segundos.")

    # Exercício 7

# print("Esse programa calcula o aumento de seu salário.")
# salario = float(input("Diga me seu salário: R$"))
# porcentagem = float(input("Diga me agora a porcentagem de aumento: "))
# aumento = salario + salario * (porcentagem/100)
# print(f"O seu salério com aumento ficará em: R${aumento:.2f}.")

    #Exercicio 8

# print("Esse programa calcula o desconto de um produto.")
# valor = float(input("Digite o preço do produto: R$"))
# porcentagem = float(input("Digite a porcentagem de desconto: "))
# desconto = valor - valor * (porcentagem/100)
# print(f"O valor do produto considerando desconto é de: R${desconto:.2f}.")

    # Exercício 9

# print("Esse programa caulcula o tempo da sua viagem de carro.")
# distancia = int(input("Diga-me a distância que você irá percorrer em km: "))
# vMedia = int(input("Diga-me a velocidade média esperada para viagem em km/h: "))
# tempo = distancia/vMedia
# print("A sua viagem tem um tempo médio de ", tempo, " horas.")

    # Exercício 10

# print("Esse programa converte graus Celsius para Fahrenheit.")
# celsius = float(input("Digite a temperatura em graus Celsius: "))
# fahrenheit = ((9*celsius)/5)+32
# print("A temperatura em fahrenheit é", fahrenheit)

    # Exercício 11

# print("Esse programa calcula o preço de um aluguel de um carro.")
# km = float(input("Digite a quantidade de km rodados: "))
# dias = int(input("Digite a quantidade de dias alugados: "))
# valor = (km * 0.15) + dias * 60
# print(f"O valor pelo aluguel do carro ficou em R${valor:.2f}.")

    # Exercício 12

# print("Esse programa calcula a seguinte formula: z = (x² + y²) / (x – y)²")
# print("Os valores de x e y serão obrigatóriamente inteiros.")
# x = int(input("Digite o valor que corresponde a x: "))
# y = int(input("Digite o valor que corresponde a y: "))
# z = (x**2 + y**2) / (x - y)**2
# print(f"O valor de z é igual a {z:.2f}.")

    # Exercicios 13

# print("Esse programa reajusta o seu salário em 35%")
# salario = float(input("Digite o seu salário atual: R$"))
# reajuste = salario + salario * 0.35
# print(f"O seu salário contando com o reajuste é igual a {reajuste:.2f}")