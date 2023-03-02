#Exercício 19
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

aluno1 = str(input("Informe o nome de um aluno: "))
aluno2 = str(input("Informe o nome de um aluno: "))
aluno3 = str(input("Informe o nome de um aluno: "))
aluno4 = str(input("Informe o nome de um aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]


print(f"O aluno escolhido foi {choice(lista)}")
