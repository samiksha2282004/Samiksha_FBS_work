 #WAP to accept 3 digit number. if first digit is double of second digit and half of third digit then display"yes, you have done it", otherwise display " please try next time".
# e.g- 428, 214 etc.
num = int(input('Enter number:'))
d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10
if d1 == (2 * d2) and d1 == (d3 / 2):
    print('yes, you have done it.')
else:
    print('please try next time.')