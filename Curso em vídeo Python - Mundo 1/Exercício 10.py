#Exercício 10
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n = float(input("Informe quantos reais você possui na carteira: "))

print("Com essa quantia é possível comprar um total de {:.2f} dólares.".format(n / 3.27))