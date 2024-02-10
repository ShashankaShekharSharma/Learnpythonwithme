def addition(a,b):
  return a+b
def subtraction(a,b):
  return a-b
def multiplication(a,b):
  return a*b
def division(a,b):
  if b != 0:
    return a/b
  else:
    return "Not Possible"

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Addition: "+str(addition(a,b)))
print("Subtraction: "+str(subtraction(a,b)))
print("Multiplication: "+str(multiplication(a,b)))
print("Division: "+str(division(a,b)))
