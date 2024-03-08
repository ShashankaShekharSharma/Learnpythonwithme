'''
Questions:

You have a log file (log.txt) containing records of user activity in the following format:

timestamp|username|action

Where:
timestamp is a Unix timestamp (integer).
username is a string representing the username of the user performing the action.
action is a string representing the action performed by the user.
Write a Python program that reads the log file and performs the following tasks:

Calculate and print the total number of actions performed.
Determine and print the unique usernames present in the log.
Identify and print the most frequent action performed by users.
Assume that the log file (log.txt) is present in the same directory as your Python script.

Example log.txt content:
1614820032|user1|login
1614820125|user2|logout
1614820220|user1|upload
1614820315|user3|download
1614820408|user2|login
1614820500|user1|download
1614820592|user3|upload

Your Python script should produce output like this:
Total number of actions: 7
Unique usernames: ['user1', 'user2', 'user3']
Most frequent action: upload
'''

from collections import Counter

with open('log.txt', 'r') as file:
    log_data = file.readlines()

actions = []  # Use a different variable name for the list of actions
usernames = set()

for entry in log_data:
    timestamp, current_username, current_action = entry.strip().split('|')
    actions.append(current_action)
    usernames.add(current_username)

total_actions = len(actions)
unique_usernames = list(usernames)
most_frequent_action = Counter(actions).most_common(1)[0][0]

print(f"Total number of actions: {total_actions}")
print(f"Unique usernames: {unique_usernames}")
print(f"Most frequent action: {most_frequent_action}")

