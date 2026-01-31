basic_salary = int(input('Enter Basic salary of an employee '))
DA = (10/100 * basic_salary)
TA = (12/100 * basic_salary)
HRA = (15/100 * basic_salary)
Total_salary = basic_salary + DA + TA + HRA
print(f'Total salary of an employee is {Total_salary}')