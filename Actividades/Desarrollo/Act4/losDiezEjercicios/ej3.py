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