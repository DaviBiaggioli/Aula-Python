#Exercicio 1

# nome = "davi"
# print(nome)

#Exercicio2

# a = 3
# b = 5

#print(a*b)

#Exercicio3
# a=2
# b=6
# c=8

# print(a+b+c)

#Para números decimais é necessario fazer uma formatação de acordo com a quantidade de números que queremos após o ponto que separa os nº inteiros dos ºn fracionados:
#O f no inicio da sintax indica a separação da string da váriavel float

 # Exemplo da fora coreta:

# pi=3.1415
# print(f"O número pi com duas casas decimais é {pi:.2f}.")

#Exemplo da fora incoreta:

#pi=3.1415
#print("O número pi com duas casas decimais é ", pi, ".")

 # Exemplo de Operadores relacionais

# nota = 8
# media = 7
# aprovado = nota >= media
# print(aprovado)

# Entrada de dados
# Pra entrada de dados é necessário que declaremos a váriavel

media_final = float(input(" Média final da diciplina de 0 à 10"))
frequencia = int(input("Frequência da diciplina em porcentagem"))

if media_final >= 6 and frequencia >= 75:
    print("Aprovado!")
else:
    print("Reprovado!")




