#Exercício 20
#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input("Informe o nome de um aluno: ")
aluno2 = input("Informe o nome de um aluno: ")
aluno3 = input("Informe o nome de um aluno: ")
aluno4 = input("Informe o nome de um aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print(f"A ordem de apresentação será: {lista}")