velocidade = float(input("qual era a sua velocidade?"))

if velocidade>80:
    print("voce foi multado em RS {}".format((velocidade-80)*7))
else:
    print("você está dentro dos limites, parabéns")