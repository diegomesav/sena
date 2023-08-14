#arr1 = [1,3,5,8]
#arr2 = [2,4,6,8]
arr1 = []
arr2 = []
arr3 = []

num1 = int(input('Ingresa un numero a la lista 1: '))
arr1.append(num1)
for i in range(4):
    num = int(input('Ingresa otro numero pero debe ser mayor al anterior:  '))
    if num <= arr1[i]:
        while num <= arr1[i]:
            num = int(input(f'Recuerda que debe ser mayor que {arr1[i]}:  '))
    arr1.append(num)

num2 = int(input('Ingresa un numero a la lista 2: '))
arr2.append(num2)
for i in range(4):
    num = int(input('Ingresa otro numero pero debe ser mayor al anterior:  '))
    if num <= arr2[i]:
        while num <= arr2[i]:
            num = int(input(f'Recuerda que debe ser mayor que {arr2[i]}:  '))
    arr2.append(num)

for i in range(5):
    if arr1[i] < arr2[i]:
        arr3.append(arr1[i])
        arr3.append(arr2[i])
    else:
        arr3.append(arr2[i])
        arr3.append(arr1[i])

print(arr3)
ordenar = []

for i in range(len(arr3)):
    ordenar.append(min(arr3))
    if len(arr3) > 0:
        arr3.remove(min(arr3))

print(ordenar)