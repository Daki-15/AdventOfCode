#-----------------------------------#
#            PART 1                 #
#-----------------------------------#

# Assigning constants for color values
RED, GREEN, BLUE = 12, 13, 14
possible_game = 0  # Variable to store the sum of IDs for possible games

# Opening and reading from the "Data.txt" file
with open("Data.txt", "r") as file:
    # Iterating through each line in the file
    for lines in file:
        # Splitting the line into the ID and the record part
        id_game, record = lines.split(": ")
        _, ID = id_game.split()  # Extracting the ID

        game = True  # Variable to track if the game is possible

        # Iterating through each set of cubes in the record
        for set_of_cubes in record.split("; "):
            # Iterating through each cube in the set
            for cube in set_of_cubes.split(", "):
                value, color = cube.split()

                # Checking conditions for each color
                if "red" in color and int(value) > RED:
                    game = False
                if "green" in color and int(value) > GREEN:
                    game = False
                if "blue" in color and int(value) > BLUE:
                    game = False

        # If the game is possible, add the ID to the sum
        if game:
            possible_game += int(ID)

# Printing the result for Part 1
print(f"The sum of the IDs of possible games: {possible_game}")


#-----------------------------------#
#            PART 2                 #
#-----------------------------------#

possible_game = 0  # Resetting the variable for Part 2

# Reopening and reading from the "Data.txt" file
with open("Data.txt", "r") as file:
    # Iterating through each line in the file
    for lines in file:
        # Splitting the line into the ID and the record part
        id_game, record = lines.split(": ")
        _, ID = id_game.split()  # Extracting the ID

        game = True  # Variable to track if the game is possible
        max_red, max_green, max_blue = 1, 1, 1  # Variables to track the maximum values for each color

        # Iterating through each set of cubes in the record
        for set_of_cubes in record.split("; "):
            # Iterating through each cube in the set
            for cube in set_of_cubes.split(", "):
                value, color = cube.split()

                # Updating the maximum values for each color
                if "red" in color and int(value) > max_red:
                    max_red = int(value)
                if "green" in color and int(value) > max_green:
                    max_green = int(value)
                if "blue" in color and int(value) > max_blue:
                    max_blue = int(value)

        # If the game is possible, calculate and add the product of maximum values to the sum
        if game:
            possible_game += (max_red * max_green * max_blue)

# Printing the result for Part 2
print(f"The power of a set of cubes is equal to: {possible_game}")
