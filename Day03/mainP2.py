def is_simbol(i, j, num):
    # Check if (i, j) is within the matrix boundaries
    if not (0 <= i < rows and 0 <= j < cols):
        return False

    # If the character at (i, j) is '*', append the num to gear_ratios[i][j]
    if datas[i][j] == "*":
        gear_ratios[i][j].append(num)

    # Check if the character at (i, j) is not a dot ('.') and not a digit
    return datas[i][j] != '.' and not datas[i][j].isdigit()

def part2():
    ans = 0

    # Iterate through each line in the matrix
    for i, line in enumerate(datas):
        start = 0
        j = 0

        # Process each character in the line
        while j < cols:
            start = j
            num = ""

            # Extract consecutive digits to form a number
            while j < cols and line[j].isdigit():
                num += line[j]
                j += 1

            # If no digits were found, move to the next character
            if num == "":
                j += 1
                continue

            # Convert the extracted digits to an integer
            num = int(num)

            # Number ended, look around for specific patterns
            is_simbol(i, start-1, num) or is_simbol(i, j, num)

            for k in range(start-1, j+1):
                is_simbol(i-1, k, num) or is_simbol(i+1, k, num)

    # Calculate the final result based on gear_ratios
    for i in range(rows):
        for j in range(cols):
            nums = gear_ratios[i][j]
            if datas[i][j] == "*" and len(nums) == 2:
                ans += nums[0] * nums[1]

    # Print the final result
    print(ans)

# Read data from the file and initialize rows and cols
with open("Data.txt", "r") as file:
    datas = file.read()
    datas = datas.strip().split("\n")

    rows = len(datas)
    cols = len(datas[0])

    # Initialize a 2D list for gear ratios
    gear_ratios = [[[] for _ in range(cols)] for _ in range(rows)]

# Call the main function
part2()
