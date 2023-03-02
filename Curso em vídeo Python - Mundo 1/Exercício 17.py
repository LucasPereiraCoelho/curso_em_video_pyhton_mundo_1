#Exercício 17
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

n = float(input("Informe o comprimento do cateto oposto: "))
x = float(input("Informe o comprimento do cateto adjacente: "))

hipo = (n ** 2 + x ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hipo}")

import math

print(f"A hipotenusa vai medir {math.hypot(n, x)}")