def numeros(num1,num2,num3):
    num=num1, num2, num3
    return max(num)

num1 = int (input("escolha um num: "))
num2 = int (input("escolha outro num: "))
num3 = int (input("escolha mais um num: "))
 
print("o maior numero é: ",numeros (num1,num2,num3))