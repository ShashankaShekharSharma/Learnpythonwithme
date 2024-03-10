# A clockwise rotation of a list consists of taking the last element and moving it to the beginning of the list. For instance if we rotate the list, [4,5,1,2,3] we get [5,1,2,3,4]. Your task is to perform k rotations of a list
#The first line of the input contains a non empty sequence of comma separated integers. The second line of the input is a positive integer k. Perform k rotations of the list and print it as a sequence of comma separated integers. The second line of integer is a positive integer k. Perform k rotations of the list and print it as a sequence of comma separated values
def rotate(L):
    L.insert(0,L.pop())
    return L
L = [1,2,3,4,5]
k = int(input())
for i in range(k):
    L = rotate(L)
print(L)