#1 Escreva um programa que soma dois números inteiros inseridos pelo usuário

print("Vamos somar ?")

primeiro_numero = int(input("Digite um número inteiro: "))

segundo_numero = int(input("Digite outro número inteiro: "))

soma = primeiro_numero + segundo_numero

print(f"A soma entre {primeiro_numero} e {segundo_numero} é igual a {soma}")




# 2.	Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5

print("Vamos calcular o resto da divisão de um número qualquer por 5 ?")

numero = float(input("Digite um número para dividirmos por 5: "))

resto = numero % 5

print(f"O resto da divisão de {numero} por 5 é igual a {resto}")


# 3.	Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado

print("Que tal fazermos a multiplicação de dois números ?")

primeiro_numero = int(input("Digite um número inteiro: "))

segundo_numero = int(input("Digite outro número inteiro: "))

mult = primeiro_numero * segundo_numero

print(f"O resultado da multiplicação entre {primeiro_numero} e {segundo_numero} é igual a {mult}")


# 4.	Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo

print("Agora vamos nos divertir fazendo uma divisão ?")

dividendo = int(input("Digite o número a ser dividido (dividendo) : "))

divisor = int(input("Agora digite o número para dividir o anterior (divisor) : "))

quociente = dividendo // divisor

print(f"O resultado da divisão inteira entre {dividendo} e {divisor} é igual a {quociente}")



# 5.	Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero = int(input("Digite um número inteiro: "))

quadrado = (numero * numero)

print(f"O quadrado do número {numero} é igual a {quadrado}")



# 6.    Escreva um programa que receba dois números flutuantes e realize sua adição.

print("Vamos somar ?")

primeiro_numero = float(input("Digite um número: "))

segundo_numero = float(input("Digite outro número: "))

soma = primeiro_numero + segundo_numero

print(f"A soma entre {primeiro_numero} e {segundo_numero} é igual a {soma}")

# 7.    Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

print("Vamos calcular a média ?")

primeiro_numero = float(input("Digite um número: "))

segundo_numero = float(input("Digite outro número: "))

media = (primeiro_numero + segundo_numero) / 2

print(f"A média entre {primeiro_numero} e {segundo_numero} é igual a {media}")

# 8.    Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

print("Quer descobrir a potência de um número ?")

primeiro_numero = int(input("Digite um número para ser a base: "))

segundo_numero = int(input("Agora digite o expoente: "))

potencia = primeiro_numero ** segundo_numero

print(f"{primeiro_numero} elevado a {segundo_numero} potência é igual a {potencia}")


# 9.    Faça um programa que converta a temperatura de Celsius para Fahrenheit.

print("Você sabia que nos EUA o pessoal mede a temperatura em º Fahrenheit ?")

temperatura_c = float(input("Digite uma temperatura aqui no Brasil em Celsius: "))

temperatura_f = float((temperatura_c * 9 / 5) + 32)


print(f"Quando aqui no Brasil está {temperatura_c} graus Celsius,eu agora sei que é o equivalente a {temperatura_f} graus Fahrenheit")



# 10.   Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

print("Vamos calcular a área de um círculo ?")

raio = float(input("Digite o raio do círculo: "))

area = float(3.14 * raio * raio)

print(f"A área de um círculo com raio de {raio} é {area}")

