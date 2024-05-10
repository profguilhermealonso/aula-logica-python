# Calculadora de IMC

# Solicita os valores ao usuário
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print("Seu IMC é:", imc)