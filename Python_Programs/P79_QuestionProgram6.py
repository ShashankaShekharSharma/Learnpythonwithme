# The scores_dataset is a list of dictionary one of whose entries is given below for your reference
#{'SeqNo':1,'Name':'Devika','Gender':'F','City':'Bengaluru','Mathematics':85,'Physics':100,'Chemistry':79,'Biology':75,'Computer Science':88,'History':60,'Civics':88,'Philosophy':95}
# An institution decides to allow students to create student groups for each subject where students with similar marks can help each other. But it draws up a set of constraints for creating student groups:
# A group should be associated with particular subject
# The difference between the scores of any two students in the group should be at most mark_limit.
# It follows that multiple groups can be formed for a given subject.
# Write a function called crowded_group that accepts three arguments as input: scores_dataset, subject, mark_limit
#Return the size of the largest possible group in this subject with the given mark_limit
def crowded_group(scores,sub,limit):
    lis = []
    for st in scores:
        lis.append(st[sub])
    lis.sort()
    grp = 0
    for i in range(len(lis)):
        for j in range(len(lis)):
            if lis[j]-lis[i] <= limit:
                if j - i + 1 > grp:
                    grp = j - i + 1
    return grp