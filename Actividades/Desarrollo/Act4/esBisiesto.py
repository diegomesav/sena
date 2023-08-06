from datetime import datetime
#from datetime import timedelta
#from dateutil.relativedelta import relativedelta

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


agno = int(input("Ingresa el año en que naciste:  "))
mes = int(input("Ingresa el mes en que naciste:  "))
dia = int(input("Ingresa el dia en que naciste:  "))

fecha_nacimiento = datetime(agno, mes, dia) 
fecha_actual = datetime.now()
edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

print(f"La edad es: {edad} años")