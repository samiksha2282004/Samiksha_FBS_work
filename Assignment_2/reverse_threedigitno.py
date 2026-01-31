Number = int(input('Enter three digit number '))
remainder_1 = Number % 10
Number = Number // 10
remainder_2 = Number % 10
Number = Number // 10
remainder_3 = Number % 10
rev = remainder_1 * 100 + remainder_2 * 10 + remainder_3
print(f'Reverse of three digit number is {rev}')