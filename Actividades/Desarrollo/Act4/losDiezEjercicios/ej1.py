print('ejercicio 1:')

distanciaTotal = 42.195
#Tiempo transcurrido: 2 horas y 25 minutos
tiempoMin = (2*60) + 25
promedioMin = distanciaTotal / tiempoMin
minKilomtro = round((1 / promedioMin),1)

print(f"El atleta completo la carrera a una velocida de {promedioMin} Km por minuto \n Es decir que tardaba {minKilomtro} minutos para recorrer un Km")