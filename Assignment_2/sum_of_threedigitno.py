Number = int(input('Enter three digit number '))
remainder_1 = Number % 10
Number = Number // 10
remainder_2 = Number % 10
Number = Number // 10
remainder_3 = Number % 10
Number = Number // 10
Sum = remainder_1 + remainder_2 + remainder_3
print(f'sum of three digit number is {Sum}')