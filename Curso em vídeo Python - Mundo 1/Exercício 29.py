#Exercício 29
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input("Informe a velocidade do carro em Km/h: "))

if vel > 80:
    print(f"Você será multado em R$ {(vel - 80) * 7} reais.")
else:
    print(f"Parabéns, você conduz com segurança.")