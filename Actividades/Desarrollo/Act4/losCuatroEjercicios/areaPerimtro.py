def opcion ()-> int:
    return int(input())

def area_perimetro():
    return input('por favor presiona "a" si deseas saber el area o "p" si deseas el perimetro:  ')
    

def area_triangulo():
    base = float(input('Ingrese la base:  '))
    altura =float(input('Ingrese la altura:  '))
    print(f'El area de ese triangulo es: {round((base*altura)/2)}')

def perimetro_triangulo():
    lado1 = float(input('Ingrese el lado 1:  '))
    lado2 = float(input('Ingrese el lado 2: '))
    lado3 = float(input('Ingrese el lado 3:  '))
    print(f'El perimetro de ese triangulo es: {lado1 + lado2 + lado3}')

def area_rectangulo():
    base = float(input('Ingrese la base:  '))
    altura =float(input('Ingrese la altura:  '))
    print(f'El area de ese rectangulo es: {round(base*altura)}')

def perimetro_rectangulo():
    base = float(input('Ingrese la base:  '))
    altura =float(input('Ingrese la altura:  '))
    print(f'El perimetro de ese rectangulo es: {round(2*(base + altura))}')

def area_cuadrado():
    lado = float(input('Ingrese la medida de un lado:  '))
    print(lado**2)

def perimetro_cuadrado():
    lado = float(input('Ingrese la medida de un lado:  '))
    print(lado**2)

def area_circulo():
    import math
    radio = float(input('Ingrese la medida del radio:  '))
    print(f'El area de ese circulo es:  {round(math.pi * (radio **2 ),2)}')

def perimetro_circulo():
    import math
    radio = float(input('Ingrese la medida del radio:  '))
    print(f'El perimetro de ese circulo es:  {round((math.pi * radio * 2),2) }')

print("""
Seleccione el numero de la figura que desea consultar:
1. Triangulo
2. Rectangulo
3. cuadrado
4. Circulo""")

opcion = opcion()

if area_perimetro() == 'a':
    if opcion == 1:
        area_triangulo()
    elif opcion == 2:
        area_rectangulo()
    elif opcion == 3:
        area_cuadrado()
    elif opcion == 4:
        area_circulo() 

else:
    if opcion == 1:
        perimetro_triangulo()
    elif opcion == 2:
        perimetro_rectangulo()
    elif opcion == 3:
        perimetro_cuadrado()
    elif opcion == 4:
        perimetro_circulo() 
    