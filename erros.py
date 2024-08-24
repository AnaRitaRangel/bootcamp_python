# 4.    Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo

try:
    print("Agora vamos nos divertir fazendo uma divisão ?")
    dividendo = int(input("Digite o número a ser dividido (dividendo) : "))
    divisor = int(input("Agora digite o número para dividir o anterior (divisor) : "))
    quociente = dividendo // divisor
    print(f"O resultado da divisão inteira entre {dividendo} e {divisor} é igual a {quociente}")
except:ZeroDivisionError
print("integer division or modulo by zero")

# # Exemplo que causa TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(e)


