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


# 4.    Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo
try:
    print("Agora vamos nos divertir fazendo uma divisão ?")
    dividendo = int(input("Digite o número a ser dividido (dividendo) : "))
    divisor = int(input("Agora digite o número para dividir o anterior (divisor) : "))
    quociente = dividendo // divisor
    print(f"O resultado da divisão inteira entre {dividendo} e {divisor} é igual a {quociente}")
except ZeroDivisionError:
    print("integer division or modulo by zero")


# 5.    Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

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

import math

print("Vamos calcular a área de um círculo ?")

raio = float(input("Digite o raio do círculo: "))

area = float(math.pi * raio ** 2)

print(f"A área de um círculo com raio de {raio} é {area:.2f}")

# 11.	Escreva um programa que receba uma string do usuário e a converta para maiúsculas

nome = input("Digite qualquer frase em letras maiúsculas: ")

print(f"Essa frase em letras minúsculas fica assim: {nome.lower()}")


# 12.	Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome = input("Digite seu nome completo em letras minúsculas: ")

print(f"Seu nome em letras maiúsculas fica assim: {nome.upper()}")


# 13.	Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Digite qualquer frase: ")

frase_editada = frase.strip()

print(f"Essa frase sem espaços no início ou final fica assim: {frase.strip()}")


# 14.	Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("digite a data do seu aniversário no formato dd/mm/aaaa")

dia, mes, ano = data.split("/")
print("Dia: ", dia)
print("Mês: ", mes)
print("Ano: ", ano)

print(f"Você nasceu no dia {dia} do mês {mes} do ano de {ano}")



# 15.	Escreva um programa que concatene duas strings fornecidas pelo usuário.

print("Você conhece ditados populares ?")

frase_1 = input("Digite a primeira parte do ditado popular: ")

frase_2 = input("Digite a segunda parte do ditado popular: ")

print(f"O ditado popular que você mencionou é {frase_1 +   frase_2}")

#16.	Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# Exemplo de entrada
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)


#17.	Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)


#18.	Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

#19.	Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

#20.	Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)
