from time import sleep

def contagem_regressiva (num):
    while num > 0:
     num = num-1
     print(num)
     sleep(1)


p = int(input("declare o valor inicial:"))
print(contagem_regressiva(p))