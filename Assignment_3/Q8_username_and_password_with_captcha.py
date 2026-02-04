import random

id = 'Samiksha'
pw = '2284'

Username = input('Enter Username: ')
Password = input('Enter Password: ')

if Username == id and Password == pw:
    print('Login successful')
else: 
    print('Login Failed')

captcha = random.randint(1000, 9999)
print(captcha)

c = int(input('Enter captcha:'))

if c == captcha:
    print('success')
else:
    print('Failed')

 