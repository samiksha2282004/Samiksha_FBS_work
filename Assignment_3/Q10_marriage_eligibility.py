gender = (input('Enter gender (M/F): '))
age = int(input('Enter age: '))
if gender == ['F' , 'f', 'Female', 'female', 'FEMALE']:
    if age >= 18:
        print('Eligible for marriage')
    else:
        print('Not Eligible')
else:
    if age >= 21:
        print('Eligible')
    else:
        print('not eligible')