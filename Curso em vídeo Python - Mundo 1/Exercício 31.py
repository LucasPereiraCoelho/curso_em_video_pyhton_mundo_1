#Exercício 31
#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Informe a distância da viagem em Km: "))

if distancia <= 200:
    print(f"O preço total da passagem será de R${distancia * 0.5  } reais.")
else:
    print(f"O preço total da passagem será de R${distancia * 0.45} reais.")