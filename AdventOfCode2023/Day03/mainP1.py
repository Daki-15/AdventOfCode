def is_simbol(i, j):
  # Check if (i, j) is within the matrix boundaries
  if not (0 <= i < rows and 0 <= j < cols):
      return False

  # Check if the character at (i, j) is not a dot ('.') and not a digit
  return datas[i][j] != '.' and not datas[i][j].isdigit()

def part1():
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

          # Look left/right
          #   j= 0 1 2 3 4 5 6 7 8 9
          # i= 0 . . . . . . . . . .
          #    1 . . . . . . . . . .
          #    2 . . X _ _ _ X . . .
          #    3 . . . . . . . . . .
          #    4 . . . . . . . . . .
          if is_simbol(i, start-1) or is_simbol(i, j):
              ans += num
              continue

          # Look up/down and diagonally
          #   j= 0 1 2 3 4 5 6 7 8 9
          # i= 0 . . . . . . . . . .
          #    1 . . X X X X X . . .
          #    2 . . . _ _ _ . . . .
          #    3 . . X X X X X . . .
          #    4 . . . . . . . . . .
          for k in range(start-1, j+1):
              if is_simbol(i-1, k) or is_simbol(i+1, k):
                  ans += num
                  break

  # Print the final result
  print(ans)

# Read data from the file and initialize rows and cols
with open("Data.txt", "r") as file:
  datas = file.read()
  datas = datas.strip().split("\n")

  rows = len(datas)
  cols = len(datas[0])

# Call the main function
part1()
