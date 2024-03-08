'''
def GradeCountCheck(grade):
    grades = []
    count = []
    grades_dict = {}
    for element in grade:
        if element not in grades:
            grades.append(element)
            count.append(grade.count(element))
    for g,c in zip(grades,count):
        grades_dict[g] = c
    custom_order = ['A','B','C','D','E','F']
    grades_dict = {key:grades_dict[key] for key in custom_order}
    return grades_dict
grade = ['C','D','A','A','B','B','A']
print(GradeCountCheck(grade))
'''
from collections import Counter
def grade_count_check(grades):
    grades_count = dict(Counter(grades))
    custom_order = ['A', 'B', 'C', 'D', 'E', 'F']
    grades_dict = {key: grades_count.get(key, 0) for key in custom_order}
    return grades_dict
grades = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
print(grade_count_check(grades))