# Calculadora de média - valor declarado na variável

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print("A média é: " + str(media))

# verifica se aluno foi APROVADO ou REPROVADO
if(media >= 7):
    print("O aluno foi aprovado. Média final foi: " + media)
else:
    print("O aluno foi reprovado. Média final foi: " + media)