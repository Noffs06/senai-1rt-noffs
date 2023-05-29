num = int(input("escolha um numero: "))

for numero in range(1,11):
    resultado = num * numero
    print("{} x {} = {}".format (num,numero,resultado))