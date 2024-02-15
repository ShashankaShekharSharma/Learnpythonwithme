def FuzzBuzz(n):
    if n%3==0 and n%5==0:
        return "FuzzBuzz"
    elif n%5==0:
        return "Buzz"
    elif n%3==0:
        return "Fuzz"
    else:
        return "Not FuzzBuzz"
for i in range(1,101):
    print(i,FuzzBuzz(i))