n = int(input('Enter number: '))
i = 1
while(i <= n):
    if(i % 2 != 0 and i % 3 != 0):
        print(f'{i} is not divisible by 2 and 3')
    i += 1