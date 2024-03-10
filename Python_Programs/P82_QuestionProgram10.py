# Accept a sequence of space-separated words as input. Each word is either a digit from "zero' to 'nine" (endpoints inclusive) or one of the two operands: "plus" or "minus". The operands and operators alternate in the sequence. In other words, no two consecutive words will be of the same type.
# You have to find the solution of this arithmetic problem and print the answer as an integer. Evaluate the expression without introducing brackets anywhere. That is, minus one plus two minus three
def evalute(s):
    temp={'zero':0,'one': 1, 'two': 2,'three':3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9}
    l=s.split('')
    result=0
    for i in range(0,len(l),2):
        if s[i] == 'plus':
            result += s[i+1]
        elif s[i] == 'minus':
            result -= s[i+1]
        else:
            if i == 0:
                result = s[i]
            else:
                if s[i-1] == 'plus':
                    result += s[i]
                elif s[i-1] == 'minus':
                    result -= s[i]
    return result
