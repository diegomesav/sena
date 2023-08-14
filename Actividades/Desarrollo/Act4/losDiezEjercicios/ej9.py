print('ejercicio 9')

factorial = int(input('Ingresa el factorial que deseas obtener:  '))
resFact = 1
for num in range(1,(factorial+1)):
    resFact *= num
print(f'El factorial de {factorial} es {resFact}')

print()