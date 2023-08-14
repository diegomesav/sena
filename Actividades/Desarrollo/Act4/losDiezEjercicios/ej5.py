print('ejercicio 5')


nums = []
print('Por favor ingresa 20 numeros diferentes')
for i in range(20):
    num = None
    while not num:
        try: 
            num = int(input(f'Numero {i + 1}: \t'))
            nums.append(num)
        except:
            num = None

for i in nums:
    if i > 25:
        print(f'{i} es mayor que 25')
print()
