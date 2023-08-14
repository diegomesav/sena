oyentes = []
for i in range(6):
    oyente = {}
    oyente['nombre'] = input('Ingresa tu nombre:  ')
    oyente['cedula'] = input('Ingresa tu cedula:  ')
    oyente['fecha de nacimiento'] = input('Ingresa tu fecha de nacimiento:  ')
    oyente['correo'] = input('Ingresa tu correo:  ')
    oyente['ciudad de origen'] = input('Ingresa tu ciudad nde origen:  ')
    oyente['ciudad de residencia'] = input('Ingresa tu ciudada de residencia:  ')
    oyente['artista favorito'] = input('Ingresa tu artista favorito:  ')
    canciones = {}
    print('ingresa tus 3 canciones favoritas.')
    canciones['1:'] = input('1:  ')
    canciones['2:'] = input('2:  ')
    canciones['3:'] = input('3:  ')
    oyente['canciones favoritas'] = canciones
    
    
    oyentes.append(oyente)
oyenteGanador = int(input("di un numero del 1 al 6 para elegir el oyente ganador:  "))
print(oyentes[oyenteGanador -1])