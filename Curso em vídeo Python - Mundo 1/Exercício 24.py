#Exercício 24
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Informe o nome da sua cidade: ")).strip()
cidade = cidade.upper()
print(cidade.startswith('SANTO'))