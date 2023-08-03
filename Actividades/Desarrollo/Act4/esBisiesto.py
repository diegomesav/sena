from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
"""
agno = ''

while agno == '':
    try:
        agno = int(input('Ingresa un año y te diré si es bisiesto o no:  '))
    except:
        print('Ingresa un año válido')
        agno = ''

if agno % 4 != 0:
    print('No es bisiesto')
elif agno % 100 != 0:
    print('Es bisiesto')
elif agno % 400 != 0:
    print('No es bisiesto')
else:
    print('Es bisiesto')

fechaCadena = "2020-04-22 00:00:00"
ahora = datetime.strptime(fechaCadena, '%Y-%m-%d %H:%M:%S')"""


fechaCadena = "2020-04-22"
ahora = datetime.strptime(fechaCadena, '%Y-%m-%d')
print(ahora.year, ahora.month, ahora.day, sep='-')

dentro_de_un_mes = ahora + relativedelta(months=-1)
print("Dentro de un mes: " + str(dentro_de_un_mes))


dentro_de_anio_y_semana = ahora + relativedelta(years=1, weeks=1)
print("Dentro de un año y una semana: " + str(dentro_de_anio_y_semana.year))

# Sumar pero con negativos, obteniendo una resta

hace_dos_anios = ahora + relativedelta(years=-2,months=-1)
print("Hace dos años: " + str(hace_dos_anios))