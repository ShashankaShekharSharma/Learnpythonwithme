sentence = input("Write the input: ")
count = 1
for i in range(len(sentence)):
    if sentence[i] == ' ':
        count +=1
print("The count of sentence is: ",count)
