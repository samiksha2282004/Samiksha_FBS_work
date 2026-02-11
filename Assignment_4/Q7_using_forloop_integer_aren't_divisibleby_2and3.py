n = int(input('Enter number: '))
for i in range(1, n):
    if(i % 2 != 0 and i % 3 != 0):
        print(f'{i} is not divisible by 2 and 3')
   