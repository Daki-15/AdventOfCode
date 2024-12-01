# Open the file named "Data.txt" in read mode and automatically close it when done
with open("Data.txt", "r") as file:
    # Read the contents of the file and split them into a list based on newline characters
    datas = file.read().split("\n")

    # Extract time and distance values from the first and second lines of the file
    _, time = datas[0].split(": ")
    _, distance = datas[1].split(": ")

    # Remove any extra whitespaces and convert time and distance to integers
    time = int("".join(time.split()))
    distance = int("".join(distance.split()))

# Define a function to calculate the number of ways based on time and distance
def calc_number_of_ways(time, distance):
    # Generate a list of possible hold values between 2 and (time - 2)
    res = [hold for hold in range(2, time-1) if (time - hold) * hold > distance]
    # Return the count of elements in the list
    return len(res)

# Call the function with the extracted time and distance values
res = calc_number_of_ways(time, distance)

# Print the result using an f-string
print(f"What do you get if you multiply these numbers together? {res}")
