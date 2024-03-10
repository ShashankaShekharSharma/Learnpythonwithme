# Para is sequence of space separated words. All words will be in lower case. There will be a single space between consecutive words. The string has no other special characters other than the space.
# Write the function named exact_count that accepts the string para and a positive integer n as arguments. You have to return True if there is atleast one word in para that occurs exactly n times, and False otherwise.
# You do not have to accept input from the user or print output in the console. You just have to write the function definition
def exact_count(para,n):
    para = para.split(" ") # Split the string into a list of words
    d = {}
    for i in para:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in d:
        if d[i] == n:
            return True
        else:
            return False
