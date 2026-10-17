num1 = int(input('Enter the first number: '))

num2 = int(input('Enter the second number: '))

num1 += 12

print('Addition:', num1 + num2)
print('Substraction:', num1 - num2)
print('MUltiplication:', num1 * num2)
print('Division:', num1 / num2)
print('Modulus:', num1 % num2)
print('Exponent:', num1 ** num2)
print('Floor Division:', num1 // num2)
print('Absolute value of/the modulus of', abs(-3))
print('Powering', pow(5, 2))
print('Round', round(5 / 7))  # ????

word = 'Hello'
print(*(word,) * 5, sep=' ')