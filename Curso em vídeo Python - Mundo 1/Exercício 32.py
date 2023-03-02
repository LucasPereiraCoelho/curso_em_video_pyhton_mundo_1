#Exercício 32
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input("Informe um ano para saber se o mesmo é bissexto, coloque 0 para saber se o ano atual é bissexto: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 4 == 0:
    print(f"Ano bissexto!")
else:
    print(f"Ano não bissexto")