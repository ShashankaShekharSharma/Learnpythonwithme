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

# Tensorflow 
Tensorflow is an open source framework that makes machine learning and neural networking easy to use

# Machine Learing
Machine Learning is a broad field that encompasses various concepts and techniques.

Machine Learning is a branch of artificial intelligence that focuses on the development of algorithms and statistical models that enables computer to learn and make predictions or decisions without being explicitly programmed. The primary goal of Machine Learning is to allow systems to automatically improve their performance on a specific task through experience and exposure of data 

## Key Concpets
1.  Data: Data make up the foundation of Machine Learning. Models learn patterns and make predictions on historical data.
2.  Features and Labels: In supervised learning, data is divided into features(input) and labels(output).
3.  Algorithms: Mathematical models that learn patterns and relationships from the data
4.  Training: During training phase, models are exposed to dataset with known outcome
5.  Testing and Evaluation: When model is tested on new, unseen dataset to generalise its performance and generalisation to new situations
6.  Prediction or Inference: Once trained, model can be deployed to make predictions or decisions on new, unseen data

## Types of Machine Learning
### Supervised Learning
Algorithm is trained on a trained dataset where each data is associated with a corresponding output. The goal is to learn mapping from input to outputs. Example: Linear Regression, Logistic Regression, Decision Trees, Support Vector Machines
### Unsupervised Learning
Algorithm deals with unlabelled data. The algorithm tries to find pattens, relationships or structures within the data without explicit guidance. Clustering and dimensionality reduction are common tasks in unsupervised learning. Popular algorithms include k-means clustering, hierarchial clustering and principal component analysis (PCA)
### Semi Supervised Learning
This approach combines between the element of both supervised and unsupervised learning. It involves training a model on a dataset that contains both labelled and unlabelled data. This approach when getting labelled data is expensive or time consuming. Popular algorithms include self traning and co training
### Reinforcement Learning
It involves an agent learning to make decisions by interacing with an environment. The agent receives feedback in the form of rewards or penalties based on actions. It is mostly used in scenarios such as game playing, robotics, and autonomous systems. Common algorithms include: Q learning, deep Q learning and policy gradients.
### Deep Learning
Subset of Machine Learning that utilizes neural networks with multiple layers to learn complex representations of data. Neural networks learn hierarchial representations of data making them well suited for tasks such as image and speech recognition. Common deep learning architecture includes convolutional neural networks (CNN) for image processing and recurrent neural networks (RNN) for sequence data.
### Self Supervised Learning
model is trained on the data itself without explicit data labels. It involves creating labels from the data often by creating artificial tasks. Eg. Word Embedding in Natural Language Processing (model predicts missing words in the sentence)
### Transfer Learning
It involves training a model on a certain task and then leveraging that knowledge to perform well on different but related task. This is useful when labelled data for the target task is limited.

## Applications of Machine Learning
1. Image and Speech Recognition: facial recognition, object detection, speech to text conversion. Eg. Siri and Alexa
2. Natural Language Processing: sentiment analysis, chatbot, language translation, text summarisation. 
3. Recommendation Systems
4. Healthcare: disease diagnosis, patient risk prediction, personalised treatmenrt plans
5. Finance: credit scoring, fraud detection, algorithmic trading, customer service
6. Autonomous Vehicles: object detection, path planning, real time decision making
7. Predictive Maintenance: prediction of equipment failures
8. Cybersecurity: intrusion detection systems and malware detection
9. Energy Management: smart grid manaegement, predictive management in energy sector
10. Marketing and Customer Analysis: Customer Segmentation, targeted advertising, churn prediction
11. Agriculture: Satellite imagery from crop monitoring and predicting optimal harvest times
12. Human Resources: applicant tracking systems, predicting employee turnover
13. Climate Modelling: predicting weather conditions patterns, analyzing climate data, modelling environmental changes

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