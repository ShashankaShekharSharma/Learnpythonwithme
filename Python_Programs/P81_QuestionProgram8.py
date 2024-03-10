# In a portal login website, you are asked to right a function, get_password_strength to decide the strength of the password
#The strength is decided based on the total score of the password
#If the password has length greater than 7, then score increases by 1 point.
#If the password has one uppercase and one lowercase, alphabet score increases by 1 point
#If the password has atleast 1 number and no consecutive numbers like 12 or 234, then the score increases by 1 point
#If the password has atleast one special character, the password strength increases by 1 point
#If password contains username, then it is invalid
#If the password has score of 4 points, 3 points, 2 points or 1 point then print very strong, strong, moderate or weak respectively. If the password is invalid, print PASSWORD SHOULD NOT CONTAIN USERNAME and if the score is 0 then print use a different password. The arguments to the password is username and password which are already defined
def get_password_strength(username, password):
    point = 0
    if len(password)>7:
        point += 1
    if any(i.isupper() for i in password) and any(i.islower() for i in password):
        point += 1
    if any(i.isdigit() for i in password):
        point += 1 
    if any(char.isdigit() for char in password) and all(int(password[i]) != int(password[i+1]) - 1 for i in range(len(password)-1)):
        point+=1
    special_characters = "!@#$%^&*()-+"
    if any(char in special_characters for char in password):
        score += 1
    if username in password:
        return "PASSWORD SHOULD NOT CONTAIN USERNAME"
    if score == 0:
        return "Use a different password"
    if score == 1:
        return "Weak"
    if score == 2:
        return "Moderate"
    if score == 3:
        return "Strong"
    if score == 4:
        return "Very Strong"
    