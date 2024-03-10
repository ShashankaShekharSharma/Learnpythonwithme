# Two vectors are orthogonal to each other if their dot product is zero. Write a function orthogonal that accepts two arguments:
#L : List of vectors that is represented as list of lists
#v : A vector that is represented as a list
#Return the number of vectors in the list that are orthogonal to the vector v
def orthogonal(L,v):
    count = 0
    for i in L:
        for j in range(len(i)):
            dot += i[j] * v[j]
        if dot == 0:
            count += 1
    return count