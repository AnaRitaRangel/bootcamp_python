# 4.    Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo

try:
    print("Agora vamos nos divertir fazendo uma divisão ?")
    dividendo = int(input("Digite o número a ser dividido (dividendo) : "))
    divisor = int(input("Agora digite o número para dividir o anterior (divisor) : "))
    quociente = dividendo // divisor
    print(f"O resultado da divisão inteira entre {dividendo} e {divisor} é igual a {quociente}")
except ZeroDivisionError:
    print("integer division or modulo by zero")

    

## PROBLEMA: Quando vou fazer try/except depois do except ele dá erro de indentação em baixo e se eu tiro a indentação ele dá o print do que não devia
