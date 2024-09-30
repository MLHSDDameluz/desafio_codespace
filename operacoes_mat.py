# Vamos solicitar dois números inteiros e qual operação matemática devemos executar.
# Por fim apresentar o resultado da operação.

# Solicita ao usuário dois números inteiros
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Solicita ao usuário que escolha a operação matemática
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação de acordo com a escolha do usuário
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("Resultado:", resultado)