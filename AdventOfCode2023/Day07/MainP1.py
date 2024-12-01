from functools import cmp_to_key
from collections import defaultdict

# Read data from file and split into lines
with open("Data.txt", "r") as file:
    datas = file.read().strip().split("\n")

# Define the order of card labels
labels = "AKQJT98765432"

# Function to determine the type of hand
def get_type(hand):
    counts = defaultdict(int)

    # Count occurrences of each label in the hand
    for x in hand:
        counts[x] += 1
    amounts = sorted(counts.values())

    # Check for different hand types
    if amounts == [5]:
        return 5 
    if amounts == [1, 4]:
        return 4 
    if amounts == [2, 3]:
        return 3.5 
    if amounts == [1, 1, 3]:
        return 3 
    if amounts == [1, 2, 2]:
        return 2.5
    if amounts == [1, 1, 1, 2]:
        return 2
    return 1

# Function to compare two hands
def compare(a, b):
    rankA = (get_type(a), a)
    rankB = (get_type(b), b)

    # Compare based on hand type
    if rankA[0] == rankB[0]:
        if a == b:
            return 0
        # Compare based on labels if hand types are the same
        for i, j in zip(a, b):
            if labels.index(i) < labels.index(j):
                return 1
            if labels.index(i) > labels.index(j):
                return -1
        return -1
    # Compare based on hand type
    if rankA[0] > rankB[0]:
        return 1
    return -1

# Convert data into a list of tuples with labels and values
lines = []
for line in datas:
    line = line.split()
    lines.append((line[0], int(line[1])))

# Sort the lines using the compare function
lines = sorted(lines, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))

# Calculate the final result
ans = 0
for i, line in enumerate(lines):
    ans += (i + 1) * line[1]

# Print the result
print(ans)
