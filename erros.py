# Exemplo que causa TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro


# Exemplo de Type Check
numero = 10
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

# Type Check - checar o tipo da variável digitada
numero = int(input("Digite um número : "))
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

# Exemplo Try/Except/Else
try:
    resultado = len("Ana")
except TypeError as e:
    print(e)  # Imprime a mensagem de erro
else:
    print("Tudo correu bem")
finally
    print("O importante é participar")

# Exemplo de Type Conversion
numero_inteiro = 5
numero_flutuante = 2.5
# Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5

# Modifiquei o Exemplo de Type Conversion
numero_inteiro = input("Digite um número inteiro : ")
numero_flutuante = float(input("Digite um número decimal : "))
# Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5

