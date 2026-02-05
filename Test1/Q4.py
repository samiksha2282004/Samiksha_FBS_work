area = int(input('Enter area: '))
cost_i = int(input('Enter cost of Interior wall: '))
cost_e = int(input('Enter cost of exterior wall: '))
cost_in = area * 8 * cost_i
cost_ex = area * 7 * cost_e
print(f'cost of painting of interior wall is {cost_in}.')
print(f'cost of painting of exterior wall is {cost_ex}.')
