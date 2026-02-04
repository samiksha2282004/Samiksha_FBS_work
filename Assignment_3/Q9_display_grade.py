Maths = int(input('Enter Maths marks: '))
Science = int(input('Enter Science marks: '))
English = int(input('Enter English marks: '))
Hindi = int(input('Enter Hindi marks: '))
Sanskrit = int(input('Enter Sanskrit marks: '))

Total = Maths + Science + English + Hindi + Sanskrit
percentage = Total/500 * 100

if percentage >= 60:
    print('First Class')
elif percentage >= 50:
    print('Second Class')
elif percentage >= 35 :
    print('Pass Class')
else:
    print('Fail')

