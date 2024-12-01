# Open the file "Data.txt" in read mode
with open("Data.txt", "r") as file:
    # Read the file content and split it into lines
    datas = file.read().split("\n")

    # Extract time and distance from the first two lines
    _, time = datas[0].split(": ")
    _, distance = datas[1].split(": ")

    # Convert time and distance strings to lists of integers
    time = list(map(int, time.split()))
    distance = list(map(int, distance.split()))

# Define a function to calculate the number of ways
def calc_number_of_ways(time, distance):
    res = [hold for hold in range(2, time-1) if (time - hold) * hold > distance]
    # Return the list of results
    return res

# Initialize an empty list to store the number of ways for each pair of time and distance
number_of_ways = []

# Iterate over the length of the time list
for i in range(len(time)):
    # Calculate the number of ways for the current pair of time and distance
    res = calc_number_of_ways(time[i], distance[i])
    # Append the number of ways to the list
    number_of_ways.append(len(res))

# Initialize a result variable to store the final product
res = 1

# Iterate over the list of number_of_ways and calculate the product
for num in number_of_ways:
    res *= num

# Print the final result
print(f"What do you get if you multiply these numbers together? {res}")
