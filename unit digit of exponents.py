import sys
while True:
    try:
        basis = int(input('Basis: '))
        exponent = int(input('Exponent: '))
        break
    except:
        print('Invalid characters/symbols used.')        
if exponent == 0 and basis == 0:
    print('This calculation is not possible.')
    sys.exit()
elif exponent < 0:
    print(f'The result of this calculation is not a natural number.')
    sys.exit()
elif exponent == 0:
    print(f'The unit digit is 1.')
    sys.exit()
numbers_list = ['']
number = basis
last_number = 'hahaha thats cool lol'
repetetive = 0
while last_number != numbers_list[0] or repetetive <= 1:
    if numbers_list[0] == '':
        numbers_list = []
    last_number = int(str(number)[-1])
    numbers_list.append(last_number) #takes last digit of int
    number *= basis
    repetetive += 1
numbers_list.pop()
remainder = exponent % len(numbers_list) #gets remainder
if remainder == 0:
    print(f'The unit digit is {numbers_list[-1]}.')
else:
    print(f'The unit digit is {numbers_list[remainder-1]}.')