cost_price = float(input('Enter cost price: '))
selling_price = float(input('Enter selling price: '))
Profit = selling_price - cost_price
Loss = cost_price - selling_price
if selling_price > cost_price:
    print(f' Profit is {Profit}.')
elif cost_price > selling_price:
    print(f'Loss is {Loss}.')
else:
    print('No profit No loss')

