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

# Exemplo Try/Except/Else
try:
    resultado = len("Ana")
except TypeError as e:
    print(e)  # Imprime a mensagem de erro
else:
    print("Tudo correu bem")
finally
    print("O importante é participar")



