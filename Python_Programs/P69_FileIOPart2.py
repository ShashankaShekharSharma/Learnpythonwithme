import random
with open('numbers.txt','w') as f:
    for i in range(10):
        f.write(str(random.randint(1,10))+'\n')
with open('numbers.txt','r') as f:
    totalsum = 0
    for line in f:
        num = int(line.strip())
        totalsum += num
    print(totalsum)
