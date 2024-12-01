# Open the file "Data.txt" for reading
with open("Data.txt", "r") as file:
    # Read lines from the file, strip whitespace, and split by ": "
    datas = [line.strip().split(": ")[1] for line in file.readlines()]
    
    # Split each line further by " | " and create tuples
    datas = [(numbers[0].split(), numbers[1].split()) 
             for numbers in [line.split(" | ") for line in datas]]

# Initialize variables
points, ans, idx = 0, 0, 1
# Create a list of scratchcards with initial values set to 1
cards = [1] * len(datas)

# Function to convert a list of strings to a list of integers
def convert_to_int(array):
    return list(map(int, array))

# Loop through each pair of winning_numbers and your_numbers
for (winning_numbers, your_numbers) in datas:
    points = 0
    # Convert strings to integers
    winning_numbers = convert_to_int(winning_numbers)

    # Compare your numbers with winning numbers to calculate points
    for your_number in convert_to_int(your_numbers):
        if your_number in winning_numbers:
            points += 1

    # Update the number of scratchcards based on points
    j = idx
    for k in range(points):
        cards[j+k] += 1 * cards[idx-1]

    # Update the total points
    idx += 1 
    ans += 2 ** (points-1) if points > 0 else 0

# Print the total number of scratchcards
print(f"How many total scratchcards do you end up with? {sum(cards)}")