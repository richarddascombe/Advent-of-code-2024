# advent of code day 1 part 2
with open(r"C:\Users\crazy\Documents\MyCode\Advent\advent2024-1.txt", "r") as f:
    locations = f.read().splitlines()
answer=0
dif=0

# split the list into two lists by column and sort both
l1=sorted([int(l[:5]) for l in locations])
l2=sorted([int(l[5:]) for l in locations])

# sum the difference between the values in each list
for i,l in enumerate(l1):
    dif=abs(l1[i]-l2[i])
    answer+=dif

print(answer)

