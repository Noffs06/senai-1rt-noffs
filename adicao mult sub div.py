n1 = float(input("informe o primeiro valor: "))
n2 = float(input("informe o segundo valor: "))

imput = "adicao", "subtracao", "divisao", "multiplicacao"
imput = input("insir o metodo de calculo: adicao, subtracao,multiplicacao ou divisao(escreva do jeito que esta no exemplo): ")

if imput == "adicao":
    print(n1 + n2)
if imput == "subtracao":
    print(n1-n2)
if imput == "divisao":
    print(n1/n2)
if imput == "multiplicacao":
    print(n1*n2)