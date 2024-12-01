# Initialize an empty list
res = []

# Function to convert a single-digit number to a two-digit number
def two_digit(num):
    if len(num) == 1:
        return num + num
    elif len(num) > 2:
        return num[0] + num[-1]
    else:
        return num

# Function to replace words in a line with their corresponding numeric values
def replace_word_with_num(line):
    # Dictionary mapping words to their numeric representations
    dict = {'one': 'o1e', 'two': 't2w', 'three': 't3e', 
            'four': 'f4r', 'five': 'f5e', 'six': 's6x', 
            'seven': 's7n', 'eight':'e8t','nine': 'n9e'}

    # Iterate through the dictionary and replace words in the line
    for key, val in dict.items():
        line = line.replace(key, val)

    # Return the modified line
    return line

# Main function to read data from a file and perform operations
def main():
    # Open the file "Data.txt" in read mode
    with open("Data.txt", "r") as file:
        # Read lines from the file and remove leading/trailing whitespaces
        data = [line.strip() for line in file]

        # Iterate through each line in the data
        for line in data:
            # Replace words with numeric values in the line
            line = replace_word_with_num(line)

            # Initialize an empty string to store numeric characters
            temp = ""

            # Iterate through each character in the modified line
            for num in line:
                # Check if the character is a digit and add it to the temporary string
                if num.isdigit():
                    temp = temp + num

            # Convert the numeric string to a two-digit number and append to the list res
            res.append(int(two_digit(temp)))

    # Print the sum of the numbers in the list res
    print(f"Res: {sum(res)}")

# Call the main function
main()
