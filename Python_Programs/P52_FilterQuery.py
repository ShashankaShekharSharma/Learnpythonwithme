def filteremployee(employee_data, min_age, min_salary):
    filtered = [name for name, age, salary in employee_data if age > min_age and salary > min_salary]
    return filtered
employee_data = [('Alice', 28, 60000), ('Bob', 35, 75000), ('Charlie', 22, 50000), ('David', 40, 90000)]
min_age = int(input("Enter the minimunm age: "))
min_salary = int(input("Enter the minimun salary: "))
employee = filteremployee(employee_data,min_age,min_salary)
print("The Desired Employees are:")
for name in employee:
    print(name)
