from empleado import Empleado
from filtrarExtras import festivasYNormales

emp1 = Empleado("Diego",1864500,festivasYNormales())
print(emp1.valorHoraextraOrd())
print(emp1.valorHoraCompensatoria())
print(emp1.valorHoraExtraDomDia())
print(emp1.totalNomina())
