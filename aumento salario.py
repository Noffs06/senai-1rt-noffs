salario = float(input("informe seu salário:"))

if salario>8250:
    print("seu salário com o aumento é {}".format(salario*0.10 + salario))
elif salario<=8250:
    print("seu salário com o aumento é {}".format(salario*0.15 + salario))