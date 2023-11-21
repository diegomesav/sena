import tkinter as tk


ventana = tk.Tk()
ventana.geometry("400x300")

textField = tk.Entry(ventana)
textField.pack()

label = tk.Label(ventana)
label.pack()

"""def boxText():
    text20 = textField.get()
    label["text"] = text20
    print(text20)
    textField.delete("0","end")


button1 = tk.Button(ventana, text="click", command=boxText)
button1.pack()"""




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
    febDays = 29 if isYearLeap(year) else 28
    monthDays = [31, febDays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return monthDays[month - 1]

def mesValido():
    mes = ""
    while(mes.isnumeric() == False):
        mes = input("ingresa un numero de mes (entre 1 y 12) : ")
        if(mes.isnumeric()):
            if(int(mes) > 0 and int(mes) <13):
                return int(mes)
            else:
                mes = ""


def festivasYNormales() -> list:
    mes = mesValido()
    ano = 2023
    print(f"El mes {mes}/{ano} contiene {daysInMonth(ano, mes)} dias")
    dia = 1
    horasDia = []
    while((daysInMonth(ano, mes) +1) > dia ):
        try:
            textField = tk.Entry(ventana)
            textField.pack()

            horasLaboradas = int(input("Ingresa la cantidad de horas trabajadas el dia "+str(dia)+" : "))
            horasDia.append(horasLaboradas)
            dia+=1

            textField.delete("0","end")
        except ValueError:
            print("Por favor ingresa un valor numérico")

    #filtrar horas festivas ordinarias
    festivasOrdinarias = 0
    
    for i in range(len(horasDia)):
        #festivos enero
        if mes == 1:
            if ((i + 1) == 1 or (i + 1) == 8 or (i + 1) == 9 or (i + 1) == 15 or (i + 1) == 22 or (i + 1) == 29):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos febrero
        elif mes == 2:
            if ((i + 1) == 5 or (i + 1) == 12 or (i + 1) == 19 or (i + 1) == 26):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos marzo
        elif mes == 3:
            if ((i + 1) == 5 or (i + 1) == 12 or (i + 1) == 19 or (i + 1) == 20 or (i + 1) == 26):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos abril
        elif mes == 4:
            if ((i + 1) == 2 or (i + 1) == 6 or (i + 1) == 7 or (i + 1) == 9 or (i + 1) == 16 or (i + 1) == 23 or (i + 1) == 30):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos mayo
        elif mes == 5:
            if ((i + 1) == 1 or (i + 1) == 7 or (i + 1) == 14 or (i + 1) == 21 or (i + 1) == 22 or (i + 1) == 28):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos junio
        elif mes == 6:
            if ((i + 1) == 4 or (i + 1) == 11 or (i + 1) == 12 or (i + 1) == 18 or (i + 1) == 19 or (i + 1) == 25):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos julio
        elif mes == 7:
            if ((i + 1) == 2 or (i + 1) == 3 or (i + 1) == 9 or (i + 1) == 16 or (i + 1) == 20 or (i + 1) == 23 or (i + 1) == 30):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos agosto
        elif mes == 8:
            if ((i + 1) == 6 or (i + 1) == 7 or (i + 1) == 13 or (i + 1) == 20 or (i + 1) == 21 or (i + 1) == 27):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos septiembre 
        elif mes == 9:
            if ((i + 1) == 3 or (i + 1) == 10 or (i + 1) == 17 or (i + 1) == 24):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos octubre
        elif mes == 10:
            if ((i + 1) == 1 or (i + 1) == 8 or (i + 1) == 15 or (i + 1) == 16 or (i + 1) == 22 or (i + 1) == 29):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos nobiembre
        elif mes == 11:
            if ((i + 1) == 5 or (i + 1) == 6 or (i + 1) == 12 or (i + 1) == 13 or (i + 1) == 19 or (i + 1) == 26):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8

        #festivos diciembre   
        elif mes == 12:
            if ((i + 1) == 3 or (i + 1) == 8 or (i + 1) == 10 or (i + 1) == 17 or (i + 1) == 24 or (i + 1) == 25 or (i + 1) == 31):
                if(horasDia[i] < 9):
                    festivasOrdinarias += horasDia[i]
                else:
                    festivasOrdinarias += 8
        
    

    # filtrar horas extra festivas y horas extra ordinarias 
    totalHorasExtra = []
    for i in range(len(horasDia)):
        horasExtra = 0
        if(horasDia[i] > 8):
            
            #Evaluar horas extra Enero
            if mes == 1:
                if ((i + 1) == 1 or (i + 1) == 8 or (i + 1) == 9 or (i + 1) == 15 or (i + 1) == 22 or (i + 1) == 29):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra Febrero
            elif mes == 2:
                if ((i + 1) == 5 or (i + 1) == 12 or (i + 1) == 19 or (i + 1) == 26):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra Marzo
            elif mes == 3:
                if ((i + 1) == 5 or (i + 1) == 12 or (i + 1) == 19 or (i + 1) == 20 or (i + 1) == 26):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra Abril
            elif mes == 4:
                if ((i + 1) == 2 or (i + 1) == 6 or (i + 1) == 7 or (i + 1) == 9 or (i + 1) == 16 or (i + 1) == 23 or (i + 1) == 30):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra Mayo
            elif mes == 5:
                if ((i + 1) == 1 or (i + 1) == 7 or (i + 1) == 14 or (i + 1) == 21 or (i + 1) == 22 or (i + 1) == 28):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra junio
            elif mes == 6:
                if ((i + 1) == 4 or (i + 1) == 11 or (i + 1) == 12 or (i + 1) == 18 or (i + 1) == 19 or (i + 1) == 25):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra julio
            elif mes == 7:
                if ((i + 1) == 2 or (i + 1) == 3 or (i + 1) == 9 or (i + 1) == 16 or (i + 1) == 20 or (i + 1) == 23 or (i + 1) == 30):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra Agosto
            elif mes == 8:
                if ((i + 1) == 6 or (i + 1) == 7 or (i + 1) == 13 or (i + 1) == 20 or (i + 1) == 21 or (i + 1) == 27):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra Septiembre 
            elif mes == 9:
                if ((i + 1) == 3 or (i + 1) == 10 or (i + 1) == 17 or (i + 1) == 24):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra Octubre 
            elif mes == 10:
                if ((i + 1) == 1 or (i + 1) == 8 or (i + 1) == 15 or (i + 1) == 16 or (i + 1) == 22 or (i + 1) == 29):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra Noviembre 
            elif mes == 11:
                if ((i + 1) == 5 or (i + 1) == 6 or (i + 1) == 12 or (i + 1) == 13 or (i + 1) == 19 or (i + 1) == 26):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            #Evaluar horas extra Diciembre
            elif mes == 12:
                if ((i + 1) == 3 or (i + 1) == 8 or (i + 1) == 10 or (i + 1) == 17 or (i + 1) == 24 or (i + 1) == 25 or (i + 1) == 31):
                    horasExtra = ((horasDia[i] - 8),"festiva")
                else:
                    horasExtra = ((horasDia[i] - 8),"normal")

            totalHorasExtra.append(horasExtra)
            
            print("El día ",(i+1),"trabajaste",str(horasExtra[0]),"horas extra")
    #print(totalHorasExtra)
    horaExtraNormal = 0
    horaExtraFestiva = 0
    for i in totalHorasExtra:
        if(i[1] == "normal"):
            horaExtraNormal += i[0]
        else:
            horaExtraFestiva += i[0]

    if festivasOrdinarias > 40:
        festivasOrdinarias -= 8
        horaExtraFestiva += 8
    print("extras normales: ", horaExtraNormal)
    print("Ordinarias festivas: ", festivasOrdinarias)
    print("extras festivas: ",horaExtraFestiva)
    return [horaExtraNormal,festivasOrdinarias,horaExtraFestiva]
#print(festivasYNormales())

ventana.mainloop()