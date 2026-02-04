x = int(input('Enter first side: '))
y = int(input('Enter second side: '))
z = int(input('Enter third side: '))
if x == y and y == z:
    print('Triangle is equilateral')
elif x == y or y == z or x == z:
    print('Triangle is isoceles')
else:
    print('Triangle is scalene')