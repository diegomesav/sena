print('ejercicio 4')

capital = int(input('Ingrese el monto solicitado:  '))
interes = (float(input('Ingrese la tasa de interes mensual:  '))) / 100
meses = 0
deuda = 0

while capital > deuda:
    deuda += (capital * interes)
    meses +=1

print(f'La deuda se duplica en {meses} meses')
print(f'Osea en {meses // 12} años y {meses % 12} meses')