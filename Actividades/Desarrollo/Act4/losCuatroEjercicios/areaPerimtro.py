def opcion ()-> int:
    return int(input())

def areaPerimetro():
    return input('por favor presiona "a" si deseas saber el area o "p" si deseas el perimetro:  ')
    

def areaTriangulo():
    base = float(input('Ingrese la base:  '))
    altura =float(input('Ingrese la altura:  '))
    print(f'El area de ese triangulo es: {round((base*altura)/2)}')

def perimetroTriangulo():
    lado1 = float(input('Ingrese el lado 1:  '))
    lado2 = float(input('Ingrese el lado 2: '))
    lado3 = float(input('Ingrese el lado 3:  '))
    print(f'El perimetro de ese triangulo es: {lado1 + lado2 + lado3}')

def areaRectangulo():
    base = float(input('Ingrese la base:  '))
    altura =float(input('Ingrese la altura:  '))
    print(f'El area de ese rectangulo es: {round(base*altura)}')

def perimetroRectangulo():
    base = float(input('Ingrese la base:  '))
    altura =float(input('Ingrese la altura:  '))
    print(f'El perimetro de ese rectangulo es: {round(2*(base + altura))}')

def areaCuadrado():
    lado = float(input('Ingrese la medida de un lado:  '))
    print(lado**2)

def perimetroCuadrado():
    lado = float(input('Ingrese la medida de un lado:  '))
    print(lado**2)

def areaCirculo():
    import math
    radio = float(input('Ingrese la medida del radio:  '))
    print(f'El area de ese circulo es:  {round(math.pi * (radio **2 ),2)}')

def perimetroCirculo():
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

if areaPerimetro() == 'a':
    if opcion == 1:
        areaTriangulo()
    elif opcion == 2:
        areaRectangulo()
    elif opcion == 3:
        areaCuadrado()
    elif opcion == 4:
        areaCirculo() 

else:
    if opcion == 1:
        perimetroTriangulo()
    elif opcion == 2:
        perimetroRectangulo()
    elif opcion == 3:
        perimetroCuadrado()
    elif opcion == 4:
        perimetroCirculo() 
    