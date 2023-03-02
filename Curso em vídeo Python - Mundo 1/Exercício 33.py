#Exercício 33
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Informe o °1 valor: "))
num2 = int(input("Informe o °2 valor: "))
num3 = int(input("Informe o °3 valor: "))

if num2 > num1 and num1 < num3:
    menor = num1
elif num1 > num2 and num2 < num3:
    menor = num2
elif num1 > num3 and num3 < num2:
    menor = num3

if num2 < num1 and num1 > num3:
    maior = num1
elif num1 < num2 and num2 > num3:
    maior = num2
elif num1 < num3 and num3 > num2:
    maior = num3

print(f"O menor número digitado foi: {menor}")
print(f"O maior número digitado foi: {maior}")

