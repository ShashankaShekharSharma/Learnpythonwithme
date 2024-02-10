def fibonacci(n):
    sequence = []
    a,b = 0,1
    
    for _ in range(n):
        sequence.append(a)
        a,b = b,a+b
    return sequence
terms = int(input("Enter the number of terms to be generated: "))
result = fibonacci(terms)
print("Fibonacci Series: ",result)