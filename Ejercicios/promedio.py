n = int(input('numero de notas '))
suma = 0
for i in range(n):
    notas = float(input('ingrese la nota '))
    suma = suma + notas
print(suma/n)