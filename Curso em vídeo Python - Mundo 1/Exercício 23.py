#Exercício 23
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input("Informe um número de 0 a 9999: "))
# n = str(num)
# print(f"Unidade: {n[3]}")
# print(f"Dezena: {n[2]}")
# print(f"Centena: {n[1]}")
# print(f"Milhar: {n[0]}")


u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")

