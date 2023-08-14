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