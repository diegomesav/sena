from datetime import datetime
import requests
now = datetime.now()
year = str(now.year)
mont = str(now.month)
day = str(now.day) 

if(len(mont) == 1): mont = '0'+ mont
if(len(day) == 1): day = '0'+ day

dollar_price = None
try:
    url = 'https://trm-colombia.vercel.app/?date='+year+'-'+mont+'-'+day
    print()

    r = requests.get(url)
    data = r.json()
    dollar_price = float(data['data']['value'])
    print('Precio del dolar hoy: ',dollar_price)
except:
    print("Error. No se pudo establecer coneccion")
    print()
    dollar_price = float(input('Ingrese manualmente el precio del dolar: '))

amount_dollar = int(input('Ingrese la cantidad de dolares que quiere cambiar hoy: '))
print('Recibiras',(dollar_price*amount_dollar),'pesos')

access_key = '00eeec88-6d76-410c-9d81-85b846e7834c'
headers = {
    'X-Meteum-API-Key': access_key
}

response = requests.get('https://api.meteum.ai/v1/forecast?lat=40.71427&lon=-74.00597', headers=headers)
data = response.json()
print('La temperatura en ',data['info']['tzinfo']['name'], 'es de:',data['yesterday']['temp'],'°C')
print('Es decir:',(int(data['yesterday']['temp'])*(9/5) +32), '°F')