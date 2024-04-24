#Checkpoint 2 - CTE  Davi da Silva Biaggioli e Lucas Akira Watanabe 1ECS

print("*Esse programa identifica a situação do aluno ao final do ano, considerando as notas e a presença.")

#Entradas

#Notas semestres

semestre = 1

while semestre <= 2:
    print(f"\n Digite suas notas referente ao {semestre}º semestre:")
    Cp1 = int(input("\nDigite a nota de seu checkpoit 1 (De 0 a 100): "))
    Cp2 = int(input("Digite a nota de seu checkpoit 2 (De 0 a 100): "))
    Cp3 = int(input("Digite a nota de seu checkpoit 3 (De 0 a 100): "))

    S1 = int(input("Digite a nota da sua sprint 1 (De 0 a 100): "))
    S2 = int(input("Digite a nota da sua sprint 2 (De 0 a 100): "))

    Gs = int(input("Digite a nota da sua global solution (De 0 a 100): "))

    menor = Cp1
    somaS1Cp = Cp2 + Cp3
    if Cp2 < menor:
        menor = Cp2
        somaS1Cp = Cp1 + Cp3

    if Cp3 < menor:
        menor = Cp3
        somaS1Cp = Cp1 + Cp2

    if semestre == 1:
        mediaS1 = (((somaS1Cp + S1 + S2) / 4) * 0.4) + (Gs * 0.6)
    else:
        mediaS2 = (((somaS1Cp + S1 + S2) / 4) * 0.4) + (Gs * 0.6)
        preseca = int(input("Digite a sua frequência de presença nas aulas: "))
    semestre += 1


#Cálculos

#Média anual
mediaAnual = mediaS1 * 0.4 + mediaS2 * 0.6

#Saída
if preseca < 75:
    situacao = "reprovado"
elif mediaAnual >= 60:
    situacao = "aprovado"
elif mediaAnual < 40:
    situacao = "reprovado"
else:
    situacao = "está de exame"

print(f"\n Aluno {situacao} com a média anual de {mediaAnual}.")
