#Exercício 18
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

n = float(input("Informe o valor de um ângulo: "))

print(f"O valor do cosseno é de {math.cos(math.radians(n))}, do seno é de {math.sin(math.radians(n))} e da tangente é de {math.tan(math.radians(n))}")

