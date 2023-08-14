function opcion (){
    return parseInt(prompt(''))
}

function areaPerimetro () {
    return prompt('por favor presiona "a" si deseas saber el area o "p" si deseas el perimetro:  ')
}
    

function areaTriangulo(){
    let base = parseFloat(prompt('Ingrese la base:  '))
    let altura =parseFloat(prompt('Ingrese la altura:  '))
    //document.body.innerHTML = "<h1>Time right now is:  " + d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds() + "</h1>"
    prompt(`El area de ese triangulo es: ${(base*altura)}`)
}

function perimetroTriangulo(){
    let lado1 = parseFloat(prompt('Ingrese el lado 1:  '))
    let lado2 = parseFloat(prompt('Ingrese el lado 2: '))
    let lado3 = parseFloat(prompt('Ingrese el lado 3:  '))
    prompt(`El perimetro de ese triangulo es: ${lado1 + lado2 + lado3}`)
}

function areaRectangulo(){
    let base = parseFloat(prompt('Ingrese la base:  '))
    let altura =parseFloat(prompt('Ingrese la altura:  '))
    alert(`El area de ese rectangulo es:${Math.round(base*altura)}`)
}

function perimetroRectangulo():
    let base = parseFloat(prompt('Ingrese la base:  '))
    let altura =parseFloat(prompt('Ingrese la altura:  '))
    print(f'El perimetro de ese rectangulo es: {round(2*(base + altura))}')

function areaCuadrado():
    let lado = parseFloat(prompt('Ingrese la medida de un lado:  '))
    print(lado**2)

function perimetroCuadrado():
    let lado = parseFloat(prompt('Ingrese la medida de un lado:  '))
    print(lado**2)

function areaCirculo():
    import math
    let radio = parseFloat(prompt('Ingrese la medida del radio:  '))
    print(f'El area de ese circulo es:  {round(math.pi * (radio **2 ),2)}')

function perimetroCirculo():
    import math
    let radio = parseFloat(prompt('Ingrese la medida del radio:  '))
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