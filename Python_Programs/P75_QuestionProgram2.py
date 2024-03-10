# A Sequence of integers of even length is said to be left heavy if the sum of the terms in the left half of the sequence is greater than the sum of the terms in the right half. It is termed right heavy if the sum of the second half is greater than the first half. It is said to be balanced if both the sums are equal.
#Accept a sequence of comma separated integers as input. Determnine if the sequence is left heavy, right heavy or balanced and print this as the output.
a = list(map(int,input().split(' ')))
b = int(len(a)/2)
right_sum = 0
left_sum = 0
for i in range(b):
    left_sum += a[i]
for i in range(1,b+1):
    right_sum += a[-i]
if left_sum == right_sum:
    print("balanced")
elif left_sum > right_sum:
    print("left heavy")
else:
    print("right heavy")
