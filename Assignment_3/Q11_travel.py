#1
age1 = int(input('Enter age1: '))
ticket_amount_1 = int(input('Enter first ticket amount 1: '))
if age1 < 12:
    discount_1 = ticket_amount_1 * 0.70
elif age1 > 59:
    discount_1 = ticket_amount_1 *0.50
else:
    discount_1 = ticket_amount_1

#2
age2 = int(input('Enter age2: '))
ticket_amount_2 = int(input('Enter second ticket amount 2: '))
if age2 < 12:
    discount_2 = ticket_amount_2 * 0.70
elif age2 > 59:
    discount_2 = ticket_amount_2 *0.50
else:
    discount_2 = ticket_amount_2

#3
age3 = int(input('Enter age3: '))
ticket_amount_3 = int(input('Enter third ticket amount: '))
if age3 < 12:
    discount_3 = ticket_amount_3 * 0.70
elif age3 > 59:
    discount_3 = ticket_amount_3 *0.50
else:
    discount_3 = ticket_amount_3

#4
age4 = int(input('Enter age4: '))
ticket_amount_4 = int(input('Enter fourth ticket amount: '))
if age4 < 12:
    discount_4 = ticket_amount_4 * 0.70
elif age4 > 59:
    discount_4 = ticket_amount_4 *0.50
else:
    discount_4 = ticket_amount_4

#5
age5 = int(input('Enter age5: '))
ticket_amount_5 = int(input('Enter fifth ticket amount: '))
if age5 < 12:
    discount_5 = ticket_amount_5 * 0.70
elif age5 > 59:
    discount_5 = ticket_amount_5 *0.50
else:
    discount_5 = ticket_amount_5

total = discount_1 + discount_2 + discount_3 + discount_4 + discount_5
print(f'total for all {total}')


