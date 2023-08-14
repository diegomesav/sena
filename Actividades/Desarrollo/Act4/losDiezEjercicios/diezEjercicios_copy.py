import requests
from datetime import datetime
# 1--------------------------------------------------------------------------
print('ejercicio 1:')

distanciaTotal = 42.195
#Tiempo transcurrido: 2 horas y 25 minutos
tiempoMin = (2*60) + 25
promedioMin = distanciaTotal / tiempoMin
minKilomtro = round((1 / promedioMin),1)

print(f"El atleta completo la carrera a una velocida de {promedioMin} Km por minuto \n Es decir que tardaba {minKilomtro} minutos para recorrer un Km")

print()
# 2-------------------------------------------------------------------
print('ejercicio 2')


gradosC = float(input('Por favor ingrese la cantidad de grados °C que desea convertir a grados °F:  '))
print(gradosC,'grados °C son el equivalente a',(((gradosC)*(9/5)) +32), 'grados °F')

print()
# 3---------------------------------------------------------
print('ejercicio 3')

conceptos = ['taller 1','taller 2','quiz','parcial']
proporciones = [0.1,0.1,0.1,0.7]
resultados = []
materia = 0

for i in conceptos:
    calificacion = float(input(f'Ingrese la nota correspondiente al {i}:  \t'))
    resultados.append(calificacion)

for i in range(len(resultados)):
    materia += (resultados[i] * proporciones[i])

print(f'la materia te quedo en {round(materia,1)}')

print()
# 4----------------------------------------------------------------
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

print()
# 5-------------------------------------------------------------
print('ejercicio 5')


nums = []
print('Por favor ingresa 20 numeros diferentes')
for i in range(20):
    num = None
    while not num:
        try: 
            num = int(input(f'Numero {i + 1}: \t'))
            nums.append(num)
        except:
            num = None

for i in nums:
    if i > 25:
        print(f'{i} es mayor que 25')
print()
# 6-------------------------------------------------------------
print('ejercicio 6')


#Para este ejercicio por favor instalar request
#  API para obtener el precio actual del dolar

now = datetime.now()
year = str(now.year)
mont = str(now.month)
day = str(now.day) 
#  validacion para crear el formato de la consulta al API
if(len(mont) == 1): mont = '0'+ mont
if(len(day) == 1): day = '0'+ day

url = 'https://trm-colombia.vercel.app/?date='+year+'-'+mont+'-'+day

r = requests.get(url)
data = r.json()
dollar_price = float(data['data']['value'])

precios = []

for i in range(5):
    precio = float(input(f'Precio camiseta {i + 1} en dolares: \t'))
    precios.append(precio)

print(f'El total en pesos de las camisetas es:  {sum(precios) * dollar_price}')

print()
# 7--------------------------------------------------------------------------
print('ejercicio 7')


pagosClientes = {}
otroCliente = 's'

while otroCliente.lower().startswith('s'):
    nombreCliente = input('Ingresa el nombre del cliente:  ')
    pagoCliente = int(input('Total consumo:  '))
    #se aplica el 20% si le venta es mayor a 50000
    if pagoCliente > 50000: 
        pagoCliente -= (round(pagoCliente * 0.2))
    print(f'Total a pagar:  {pagoCliente}')
    pagosClientes[nombreCliente] = pagoCliente
    otroCliente = input('Hay alguien mas en la lista? (s/n):  ')
print()

print('Las ventas de hoy fueron las siguentes: ')
totalVentas = 0
for cliente in pagosClientes.items():
    print(f'{cliente[0]} \t: {cliente[1]}')
    totalVentas += cliente[1]
print(f'Hoy se vendieron {totalVentas} pesos.')

print()
# 8---------------------------------------------------------------------
print('ejercicio 8')

import time
prueba = 0
while True:
    result = time.strftime("%H : %M : %S")
    print(result)
    time.sleep(1)
    prueba += 1
    if prueba > 80:
        print('Es suficiente para ver que funciona!')
        break


print()
# 9----------------------------------------------------------------------
print('ejercicio 9')

factorial = int(input('Ingresa el factorial que deseas obtener:  '))
resFact = 1
for num in range(1,(factorial+1)):
    resFact *= num
print(f'El factorial de {factorial} es {resFact}')

print()
# 10--------------------------------------------------------------------
print('ejercicio 10')

tabla = int(input('Ingresa el numero de la tabla que quieres ver:  '))
for i in range(10,0,-1):
    print(f'{tabla} X {i} = {tabla * i}')



