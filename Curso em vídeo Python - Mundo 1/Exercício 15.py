#Exercício 15
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Informe quantos Km foram percorridos com o carro: "))
dia = int(input("Informe por quantos dias o carro foi utilizado: "))

print(f"Sabendo que a taxa diária é de 60 reais e adiciona-se 0.15 reais por quilometro, o total é de: {(km * 0.15) + (dia * 60)}")