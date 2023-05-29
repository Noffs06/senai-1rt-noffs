def numeros(n1,n2):
    num = n1, n2
    somar = n1 + n2
    multiplicar = n1 * n2
    Mn = max(num)
    mn = min(num)
    a = input('Insira uma operação: a)somar, b)multiplicar, c)valor maximo, d)valor minimo (digite a,b,c ou d): ')
    if a == 'a':
        return somar
    if a == 'b':
        return multiplicar
    if a == 'c':
        return Mn
    if a == 'd':
        return mn

a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))

print('o resultado é: ', numeros(a,b))
