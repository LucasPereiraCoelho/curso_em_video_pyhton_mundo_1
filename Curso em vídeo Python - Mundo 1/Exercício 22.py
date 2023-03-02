#Exercício 22
#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = str(input("Informe o seu nome completo: ")).strip()

print(f"Maiúsculas: {nome.upper()}")
print(f"Minúsculas: {nome.lower()}")
print(f"A quantidade de letras do nome desconsiderando os espaços é de: {len(nome) - nome.count(' ')}")
print(f"Seu primeiro nome tem: {nome.find(' ')} letras")
