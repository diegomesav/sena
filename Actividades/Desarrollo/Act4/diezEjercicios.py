import requests
from datetime import datetime

# 3---------------------------------------------------------
"""
conceptos = ['taller 1','taller 2','quiz','parcial']
proporciones = [0.1,0.1,0.1,0.7]
resultados = []
materia = 0

for i in conceptos:
    calificacion = float(input(f'Ingrese la nota correspondiente al {i}:  \t'))
    resultados.append(calificacion)

for i in range(len(resultados)):
    materia += (resultados[i] * proporciones[i])

print(f'la materia te quedo en {round(materia,1)}')"""

# 4----------------------------------------------------------------

"""capital = int(input('Ingrese el monto solicitado:  '))
interes = (float(input('Ingrese la tasa de interes mensual:  '))) / 100
meses = 0
deuda = 0

while capital > deuda:
    deuda += (capital * interes)
    meses +=1

print(f'La deuda se duplica en {meses} meses')
print(f'Osea en {meses // 12} años y {meses % 12} meses')"""

# 5-------------------------------------------------------------

"""
nums = []
print('Por favor ingresa 20 numeros diferentes')
for i in range(20):
    num = int(input(f'Numero {i + 1}: \t'))
    nums.append(num)

for i in nums:
    if i > 25:
        print(f'{i} es mayor que 25')"""

# 6-------------------------------------------------------------

now = datetime.now()
year = str(now.year)
mont = str(now.month)
day = str(now.day) 

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



