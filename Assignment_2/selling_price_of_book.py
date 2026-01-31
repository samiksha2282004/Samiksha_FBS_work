Cost_price = int(input('Enter cost price value '))
Discount = int(input('Enter Discount in percentage '))
Selling_price = Cost_price * (1-Discount/100)
print(f'Sellig price of book based on cost price and discount is {Selling_price}')