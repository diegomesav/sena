import requests
from datetime import datetime
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