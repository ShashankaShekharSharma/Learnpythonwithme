# The scores_dataset is a list of dictionary one of whose entries is given below for your reference
#{'SeqNo':1,'Name':'Devika','Gender':'F','City':'Bengaluru','Mathematics':85,'Physics':100,'Chemistry':79,'Biology':75,'Computer Science':88,'History':60,'Civics':88,'Philosophy':95}
# A student X can mentor another student Y in subject if the following conditions are fulfilled.
# 1. 10<=X.subject - Y.subject <=20
# 2. Write a function named mentor that takes the following arguments : scores, subject
#The function should return a dictionary with the following: Key: Sequence number of the student; Value: list of SeqNo of students who can be mentored by the above student
def mentors(scores_dataset,subject):
    L = {}
    for student in scores_dataset:
        L[student["SeqNo"]] = []
        for j in scores_dataset:
            marks = student[subject] - [subject]
            if 10<=marks<=20:
                L[student["SeqNo"]].append(j['SeqNo'])
    return L