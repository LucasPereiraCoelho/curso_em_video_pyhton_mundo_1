#Exercício 11
#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = float(input("Informe a altura da parede que será pintada: "))
larg = float(input("Informe a largura da parede que será pintada: "))
area = larg * alt
tinta = area / 2

print(f"Será necessário um total de {tinta} litros para pintar a parede")