#Exercício 28
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

num = randint(0, 5)

vlr = int(input("Chute um valor de 0 a 5: "))

if vlr == num:
    print("Parabéns você acertou.")
else:
    print(f"Que pena, a resposta era {num}")