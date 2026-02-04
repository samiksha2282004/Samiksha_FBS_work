x = int(input('Enter first side: '))
y = int(input('Enter second side: '))
z = int(input('Enter third side: '))

if x > 0 and y > 0 and z > 0 and (x + y > z) and (x + z > y) and (y + z > x):
    print('Triangle is valid.')
else:
    print('Triangle is not valid.')
