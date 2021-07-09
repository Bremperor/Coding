# n employees
n=5

employees=[]

for i in range(0, n):
    employee_hour=int(input("Enter your hours: "))
    employees.append(employee_hour)

total_pay=0
for i in range(0, n):
    total_pay+=employees[i]*14.25

print("Total pay: ", total_pay)