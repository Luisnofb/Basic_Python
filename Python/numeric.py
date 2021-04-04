"""
Type numeric
"""
num = 5 // 2
print(num)
print(num % 2)
num2 = int(input(":"))
if num2 % 2 == 0:
    print(num2 ** num)
else:
    print(num2 ** 3)

#
x = input(':')
if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'):
    print(f'safe {1_000_000}')
else:
    print('not safe')
#

valor = 1_000
valor += 1
print(f'{valor} and {type(valor)}')
