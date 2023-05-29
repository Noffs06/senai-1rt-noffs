def verificar_par (n):
    if n %2 ==0:
        return True
    else:
        return False
    
p = int(input("coloque um numero e verificarei se ele é par:  "))
print(verificar_par(p))
