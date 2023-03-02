#Exercício 25
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Informe o seu nome competo: ")).strip()
nome = nome.upper()
print("SILVA" in nome)