# Python
Python is a versatile and high level programming language known for its simplicity, readability and wide range of applications created by Guido Van Rossum released in 1991. Python has gained a high popularity in various domains like web development, data science, machine learning, artificial intelligence, scripting, etc. 

# Key features of Python
1. Readability: It is designed to be clean and readable making it easy for developers to code in fewer lines of code.
2. Interpreted Language: Code execution occurs line by line making it easier for debugging and testing.
3. Cross Platform Compatibility: It is compatible in all types of platforms without any modifications.
4. Extensive Standard Library: It consists of comprehensive standard library that provides modules and packages for various tasks reducing the needs for standard libraries.
5. Dynamic Typing: It allows the developers to create variables without specifying their datatype
6. Object Oriented Programming: It supports various Object Oriented Programming Concepts like classes, inheritence and polymorphism
7. Community Support: Python is known for its large support community of experienced developers contributing to open sourse projects
8. Libraries and framework: Python has a rich ecosystem of libraries and framework that cater to various domains. For data manipulation, there are libraries like Pandas and Numpy, flask and django for web development, tensoreflow and pytorch for machine learning, etc.
9. Versatility: Python is known for its application in various fields from web developemnt to artificial intelligence.
10. Rapid Prototyping: Python is a suitable language for rapid prototyping and development.

# Applications of Python
1. Web Development
2. Data Science and Analytics
3. Machine Learning and Artificial Intellignce
4. Automation and Scripting
5. Game Development
6. Scientific Computing
7. Network Programming
8. Desktop GUI Applications

# Download Python
- Install Python from the [official website](https://www.python.org/downloads/) and get the latest version as per your needs
- Install an IDE like [VS Code](https://code.visualstudio.com/) or [Pycharm](https://www.jetbrains.com/pycharm/download/?section=mac)
- You can also use online compilers like [Replit](https://replit.com)
- To use python for data scince and analytics we can also use Jupyter Notebook via [Anaconda](https://www.anaconda.com) or [Google Colab](https://colab.research.google.com)

# Setting up virtual environment
- A virtual environment in Python is a self-contained directory that contains its own Python interpreter and a set of installed packages.
- It helps isolate the dependencies and configuration of one project from another, ensuring that different projects can have their own specific versions of libraries without conflicting with each other.

# Why Virtual Environments are Important
1. Isolation: Provide isolation between projects, preventing conflicts between different versions of packages that may be required by different projects.
2. Dependency Management: you can specify and manage the exact versions of libraries and packages required for a particular project. This ensures that the project runs consistently across different environments.
3. Clean Development Environment: allow you to maintain a clean and organized development environment by avoiding the clutter of globally installed packages. Each project can have its own dependencies without affecting the system-wide Python installation.
4. Easy Collaboration: allows you to share the specific package versions needed for the project, making it easier for team members to replicate the development environment.
5. Version Compatibility: help manage version compatibility issues, especially when dealing with libraries or packages that receive updates. You can freeze the versions to avoid unexpected changes.

## Setting up a Virtual Environment
Open the terminal
```bash
python3 -m venv venv
```
```bash
python -m venv venv
```
Activate the virtual environment
```bash
source venv/bin/activate
```
Installing Packages
```bash
pip install package_name
```
Deactivating the environment
```bash
deactivate
```
## Tips for using Virtual Environment
- Before working on your project, activate the virtual environment to ensure that you're using the correct Python interpreter and packages.
- If you're using version control (e.g., Git), include the venv directory in your .gitignore file to avoid uploading it to the repository.
- Create a requirements.txt file in your project directory that lists all the project's dependencies. This makes it easy for others to recreate the virtual environment.
- To ensure that you have the latest version of pip use
  ```bash
  pip install version --upgrade pip
  ```



## Operators in Python
1. Arithmetic Operators: +,-,*,/,//,%,**
2. Relational/Comparision Operators: ==, !=, >=, <=, <, >
3. Assignment Operators: +=, -=, /=, //=, %=, **=
4. Logical Operators: not, and, or
5. Membership Operators: in, not in
6. Identity Operators: is, is not
7. Bitwise Operators: &,|,^

`As per the concept of operator precedence not>and>or`

* Functions in a module can be found using

```python
import math
print(dir(math))
```

# List Methods
```python
a = [1,2,3,4]
a.append(3) #3 is insetered at the end of the set
a.insert(0,3) #inserts 3 at 0 index
a.remove(3) #removes the number 3 from the list. It will only remove the first occurence
a.clear() #clears the entire list
a.pop() #clears the last element in the list
a.index(3) #returns the index of 3 in the list
print(50 in a) #returns true or false depeneding upto the presence of 50 in the list
a.count(5) #returns the count of the number 5 in the list
a.sort() #sorts the list into ascending order
#To get a list in descending order:
a.sort()
a.reverse()
#This can also be done in another way
a.sort(reverse = True)
```

# Extend method
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
```
Output
`[1,2,3,4,5,6]`

# File IO
## READING CONTENTS IN A FILE
```python
f = open('myfile.txt','r') 
contents = f.read()
print(contents)
f.close()
#This will read the contents in the file but will not create a new if this file does not exist
```
## WRITING CONTENTS IN A FILE
```python
f = open('myfile.txt','w')
f.write("Hello World")
f.close()
#This will overwrite the contents in the file but if the file is not created, it will make the file and write the text in it
```
## APPENDING CONTENTS IN A FILE
```python
f = open('myfile.txt','a')
f.write("Hello World)
f.close()
#This will append the contents in the file but if the file is not created, it will make the file and write the text in it
```
## Alternate way of writing file
```python
with open('myfile.txt',a) as f:
  f.write("Hello World")
#If we use this method, we need not do f.close()
```
`If a function is given a return statement multiple times, only the first return statement will be considered`

# Miscelleaneous Points
- Module result will be negatige if numerator is postive and denominator is negative
- Numerator negative and denominator positive will give positive remainder
- ```python print(str1.endswith("to",4,10))``` will search for to at the end in between 4th and 10th string
- a.replace() changes all the string which needs to be changed.

```python
l = [1,2,3,4]
a = l
```
This is not a the `correct method` to copy a list
```python
a[0] = 5
```
In this case it will not only change the value of index 0 in a, but also in l as well because the reference is copied in a and not the entire list
To `copy` the list we should use
```python
#This is the correct method for doing so
a = l.copy()
```
# Tuples
If a tuple consists of only one element, add a `,` next to it
```python
tup = (1) #This will be considered as an integer and not tuple
tup = (1,) #This will be considered as a tuple
```
```python
tuple.index(3,4,7) #It will return the index of 3 which lies in between the index range (4,7)
```
# Format Method
```py
sentence = "Hi, I am {} and I am from {}"
name = "John"
country = "United States of America"
print(sentence.format(name,country))
```
Output: `Hi, I am John and I am from United States of America`

```python
print(f"Hi I am {name} and I am from {country}")
price = 49.484
print(f"The cost of the item is {price:.2f}") #Output: The cost of the item is 49.48
```
# Docstrings
Docstrings are not comments it is ignored during execution but it is expected to have important information about the function
Docstring should be right below the `def function(parameters):`
```python
def area(n):
  '''Takes the length of the square as input and returns the area as output'''
  return n*n
print(area.__doc__)
```
Output: `Takes the length of the square as input and returns the area as output`

# Zen of Python
```py
import this
```
**The Zen of Python, by Tim Peters**
**Beautiful is better than ugly**.
**Explicit is better than implicit**.
**Simple is better than complex**.
**Complex is better than complicated**.
**Flat is better than nested.**
**Sparse is better than dense.**
**Readability counts.**
**Special cases aren't special enough to break the rules.**
**Although practicality beats purity.**
**Errors should never pass silently.**
**Unless explicitly silenced.**
**In the face of ambiguity, refuse the temptation to guess.**
**There should be one-- and preferably only one --obvious way to do it.**
**Although that way may not be obvious at first unless you're Dutch.**
**Now is better than never.**
**Although never is often better than *right* now.**
**If the implementation is hard to explain, it's a bad idea.**
**If the implementation is easy to explain, it may be a good idea.**
**Namespaces are one honking great idea -- let's do more of those!**

# PEP 8
PEP 8 is the Python Enhancement Proposal that provides style guide recommendations for writing code in the Python programming language. The term "PEP" stands for "Python Enhancement Proposal," and PEP 8 specifically addresses the style conventions for Python code.

PEP 8 covers various aspects of code style, including but not limited to:

1. **Indentation:**
   - Use 4 spaces per indentation level.

2. **Whitespace in Expressions and Statements:**
   - Avoid extraneous whitespace in the following situations: immediately inside parentheses, brackets, or braces, and between a trailing comma and a following close parenthesis.

3. **Imports:**
   - Imports should usually be on separate lines, and absolute imports are preferred over relative imports.

4. **String Quotes:**
   - Use single quotes for string literals unless the string contains a single quote character, in which case you should use double quotes.

5. **Whitespace in Expressions and Statements:**
   - Avoid extraneous whitespace in the following situations: immediately inside parentheses, brackets, or braces, and between a trailing comma and a following close parenthesis.

6. **Comments:**
   - Comments should be complete sentences, and they should be used sparingly. Comments that contradict the code are worse than no comments.

7. **Naming Conventions:**
   - Follow the naming conventions specified in PEP 8 for variables, functions, and classes.

8. **Programming Recommendations:**
   - PEP 8 provides recommendations on a variety of programming practices, such as using built-in functions and exceptions, handling exceptions, and organizing imports.

Adhering to PEP 8 helps maintain a consistent and readable style across Python codebases, making it easier for developers to collaborate and maintain code. Many Python developers and projects follow PEP 8 to ensure a standardized coding style.

# Sets
```py
a = {1,2,3}
b = {4,5,6}
c = {} #This will result in an empty dictioanary
a = set() #This will result in an empty set
# Order is not maintained in set
print(a.union(b)) #The result is {1,2,3,4,5,6}
print(s1.update(s2)) #The result of s1 union s2 will be stored in s1
d = {1,2,5}
print(a.intersection(d)) #The result is {2}
print(a.symmetric_differenece(d)) #It will print all the uncommon elements in both set
print(a.issuperset(b)) #It will tell if all the elements of b are present in a
print(a.issubset(b)) #It will tell if all the elements of a are present in b
```
# Dictionary
Accessing a value of a key
```py
info = {'name' : 'John'}
print(info['name'])
```
Accessing all the keys 
```py
print(info.keys())
```
Interating all the values to corresponding to every key
```py
for key in info.keys():
  print(info[key])
```
OR
```py
for key,value in info.items():
  print(f"{key} : {value}")
  #Output=> key : value
```
```py
d1 = {1 : 21, 2 : 23, 3 : 35}
d2 = {4 : 23, 5 : 32, 6 : 23}
d1.update(d2)
print(d1)
#{1 : 21, 2 : 23, 3 : 35, 4 : 23, 5 : 32, 6 : 23}
d1.popitem()
print(d1)
#{1 : 21, 2 : 23, 3 : 35, 4 : 23, 5 : 32}
d1.clear()
print(d1)
del d1[1] #Delete the key value pair 1 : 21
#{}
```
```py
student = {'name' : 'John'}
print(student[name2]) #Error
print(student.get[name2]) # No Error
```
