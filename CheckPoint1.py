#Checkpoint 1 - CTE  Davi da Silva Biaggioli e Lucas Akira Watanabe 1ECS

print("*Esse programa calcula a média anual de um aluno da FIAP")

#Entradas

#1º semestre

print("\n Digite suas notas referente ao 1º semestre:")
s1Cp1 = int(input("\nDigite a nota de seu checkpoit 1 (De 0 a 100): "))
s1Cp2 = int(input("Digite a nota de seu checkpoit 2 (De 0 a 100): "))
s1Cp3 = int(input("Digite a nota de seu checkpoit 3 (De 0 a 100): "))

s1S1 = int(input("Digite a nota da sua sprint 1 (De 0 a 100): "))
s1S2 = int(input("Digite a nota da sua sprint 2 (De 0 a 100): "))

s1Gs = int(input("Digite a nota da sua global solution (De 0 a 100): "))

#2º semestre
print("\n Digite suas notas referente ao 2º semestre:")
s2Cp1 = int(input("\nDigite a nota de seu checkpoit 1 (De 0 a 100): "))
s2Cp2 = int(input("Digite a nota de seu checkpoit 2 (De 0 a 100): "))
s2Cp3 = int(input("Digite a nota de seu checkpoit 3 (De 0 a 100): "))

s2S1 = int(input("Digite a nota da sua sprint 1 (De 0 a 100): "))
s2S2 = int(input("Digite a nota da sua sprint 2 (De 0 a 100): "))

s2Gs = int(input("Digite a nota da sua global solution (De 0 a 100): "))

#Cálculos

#Média 1º semestre
menor = s1Cp1
somaS1Cp = s1Cp2 + s1Cp3
if s1Cp2 < menor:
    menor = s1Cp2
    somaS1Cp = s1Cp1 + s1Cp3

if s1Cp3 < menor:
    menor = s1Cp3
    somaS1Cp = s1Cp1 + s1Cp2

mediaS1 = (((somaS1Cp + s1S1 + s1S2) / 4) * 0.4) + (s1Gs * 0.6)

#Média 2º semestre
menor = s2Cp1
somaS2Cp = s2Cp2 + s2Cp3
if s2Cp2 < menor:
    menor = s2Cp2
    somaS2Cp = s2Cp1 + s2Cp3

if s2Cp3 < menor:
    menor = s2Cp3
    somaS2Cp = s2Cp1 + s2Cp2

mediaS2 = (((somaS2Cp + s2S1 + s2S2) / 4) * 0.4) + (s2Gs * 0.6)

#Média anual
mediaAnual = mediaS1 * 0.4 + mediaS2 * 0.6

#Saída
if mediaAnual >= 60:
    situacao = "aprovado"
elif mediaAnual < 40:
    situacao = "reprovado"
else:
    situacao = "está de exame"

print(f"\n Aluno {situacao} com a média anual de {mediaAnual}.")
