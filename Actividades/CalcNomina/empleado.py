class Empleado():
    def __init__(self, nombre, salario, horas):
        self.nombre = nombre
        self.salario = salario
        self.horas = horas
    

        self.nomina = self.salario - (self.salario * 0.08)

        self.precioBase = self.salario / 240
        self.horaOrdNoc = self.precioBase * 1.35
        self.horaExtraOrd= self.precioBase * 1.25
        self.horaExtraNoc = self.precioBase *1.75
        self.horaOrdDomDia = self.precioBase * 1.75
        self.horaOrdDomNoct = self.precioBase * 2.1
        self.horaExtraDomDia = self.precioBase * 2
        self.horaExtraDomNoc = self.precioBase * 2.5
        self.horaCompensatoria = self.precioBase * 1.75

        self.salarioSinDeducciones = round(self.horaCompensatoria * self.horas[1]) + round(self.horaExtraDomDia * self.horas[2]) + round(self.horaExtraOrd * self.horas[0]) + self.salario
        self.salarioConDeducciones = round(self.salarioSinDeducciones - (self.salarioSinDeducciones * 0.08))
        self.AUX_TRANSPORTE = 140600

    def valorHoraOrdNoc(self):
        return self.horaOrdNoc
        
    def valorHoraextraOrd(self):
        return str(self.horas[0]) + " Horas extras ordinarias a " + str(round(self.horaExtraOrd)) + ". Total: " + str(round(self.horaExtraOrd * self.horas[0]))
       
    def valorHoraExtraNoc(self):
        return self.horaExtraNoc
        
    def valorHoraOrdDomDia(self):
        return self.horaOrdDomDia
        
    def valorHoraOrDomNoc(self):
        return self.horaOrdDomNoct * self.horas[1]
    
    def valorHoraExtraDomDia(self):
        return str(self.horas[2]) + " Horas extra festivas a " + str(round(self.horaExtraDomDia)) + ". Total: " + str(round(self.horaExtraDomDia * self.horas[2]))
    
    def valorHoraExtraDomNoc(self):
        return self.horaExtraDomNoc
    
    def valorHoraCompensatoria(self):
        return str(self.horas[1]) + " Horas compensatorias a " + str(round(self.horaCompensatoria)) + ". Total: " + str(round(self.horaCompensatoria * self.horas[1]))
    
    def totalNomina(self):
        if(self.salario < 2320000):
            return f"Total Nómina: {str(self.salarioConDeducciones + self.AUX_TRANSPORTE)}"
        else:
            return f"Total Nómina: {str(self.salarioConDeducciones)}"
