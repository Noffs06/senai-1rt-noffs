distancia = float(input("informe a distancia em km do trajeto:"))

if distancia<=200:
    print("o preco da passagem sera de RS {}".format(distancia*0.50))
elif distancia>200:
    print("o preco sera de RS {}".format(distancia*0.45))
    