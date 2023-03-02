#Exercício 34
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input("Informe o seu salário: "))

if salario > 1250:
    print(f"Parabéns você ganhou um aumento de 10%, seu novo salário é de: R${(salario * 0.1) + salario } reais.")
elif salario <= 1250:
    print(f"Parabéns você ganhou um aumento de 15%, seu novo salário é de: R${(salario * 0.15) + salario} reais.")
