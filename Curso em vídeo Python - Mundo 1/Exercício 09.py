#Exercício 9
#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

a = int(input("Informe um número inteiro para saber sua tabuada: "))

for n in range(1,11):
    print(f"{n} x {a} = {n * a}")