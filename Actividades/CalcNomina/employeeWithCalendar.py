class Employee():
   
    def __init__(self, nombre, salario, horas) -> None:
        self.nombre = nombre
        self.salario = salario
        self.haras = horas
            
    def totalNomina():
        pass



def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True   

def daysInMonth(year, month):
    monthDays = [31, febDays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    febDays = 29 if isYearLeap(year) else 28
    return monthDays[month - 1]


mes = int(input("Ingrese mes:"))
ano = 2023
print(f"El mes {mes}/{ano} contiene {daysInMonth(ano, mes)} dias")
dia = 1
horasDia = []
while((daysInMonth(ano, mes) +1) > dia ):
    try:

        horasLaboradas = int(input("Ingresa la cantidad de horas trabajadas el dia "+str(dia)+" : "))
        horasDia.append(horasLaboradas)
        dia+=1
    except ValueError:
        print("Por favor ingresa un valor numérico")
totalHorasExtra = []
for i in range(len(horasDia)):
    horasExtra = 0
    if(horasDia[i] > 8):
        
        #Se evaluan los dias festivos de junio
        if mes == 6:
            if ((i + 1) == 4 or (i + 1) == 11 or (i + 1) == 12 or (i + 1) == 18 or (i + 1) == 19 or (i + 1) == 25):
                horasExtra = ((horasDia[i] - 8),"festiva")
            else:
                horasExtra = ((horasDia[i] - 8),"normal")

        totalHorasExtra.append(horasExtra)
        
        print("El día ",(i+1),"trabajaste",str(horasExtra[0]),"horas extra")
print(totalHorasExtra)
horaNormal = 0
horaFestiva = 0
for i in totalHorasExtra:
    if(i[1] == "normal"):
        horaNormal += 1
    else:
        horaFestiva += 1

print("extras normales: ", horaNormal)
print("extras festivas: ",horaFestiva)
        
