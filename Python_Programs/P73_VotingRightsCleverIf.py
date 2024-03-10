# Clever If Ternary Operator 
age = int(input("Enter your age: "))
vote = ("Not Eligible to Vote","Eligible to Vote") [age >= 18] #False/True
print(vote)

sal = int(input("Enter Salary: "))
tax = sal*(0.1,0.2) [sal>=50000]
print(f"Your Tax is: {tax}") 