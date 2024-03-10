# Consider the list L = [1,2,1,5,4,5,4,3,4]
# Group by is an operation on the list L that does the following:
# It combines identical elements in L into a List. That is, it creates a list for each unique element in L and all the copies of this element go into this list.
# The result of a group by operation is nested list
# Write a function group_by that accepts a list of positive integers as argument. Perform a group by operation on the list and return the nested list. The input will be a non empty list
def groupby(L):
    L.sort()
    ans = []
    i = 0
    while i < len(L):
        temp = []
        temp.append(L[i])
        j = i+1
        while j<len(L) and L[i] == L[j]:
            temp.append(L[j])
            j+=1
        ans.append(temp)
        i = j
    return ans