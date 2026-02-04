number = int(input('Enter three digit number: '))
temp = number
r1 = number % 10
number = number // 10
r2 = number % 10
number = number // 10
r3 = number % 10
rev = r1 * 100 + r2 * 10 + r3
print(rev)
if rev == temp:
    print('it is a palindrome number')
else:
    print('it is not palindrome')