edades = []
menores = 0
adultos = 0
adultosM = 0
sumEdades = 0
for i in range(10):
    edad = 0
    while edad < 1 or edad > 120:
        try:
            edad = int(input("Ingrese su edad: (min 1, max 120):  "))
            if edad < 1 or edad > 120:
                print('Mmmmm no te creo, vuelve a ingresar')
        except:
            print("Por favor ingrese un numero valido entre 1 y 120:  ")
            edad = 0
    edades.append(edad)

for i in edades:
    if i < 18:
        menores += 1
    elif i >= 18 and i < 60:
        adultos += 1
    else:
        adultosM += 1
    sumEdades += i

print(f'Ingresaron {menores} menores, {adultos} adultos y {adultosM} adultos mayores')

print(f'la mayor edad ingesada fue {max(edades)} años')
        
print(f'la menor edad ingesada fue {min(edades)} años')

print(f'El promedio de edades fue {sum(edades) / len(edades)} años')