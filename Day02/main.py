#-----------------------------------#
#            PART 1                 #
#-----------------------------------#

RED, GREEN, BLUE = 12, 13, 14
possible_game = 0

with open("Data.txt", "r") as file:
  for lines in file:
    id_game, record = lines.split(": ")
    _, ID = id_game.split()
    game = True
    
    for set_of_cubes in record.split("; "):
      for cube in set_of_cubes.split(", "):
        value, color = cube.split()
        
        if "red" in color and int(value) > RED:
          game = False
        if "green" in color and int(value) > GREEN:
          game = False
        if "blue" in color and int(value) > BLUE:
          game = False
          
    if game:
      possible_game += int(ID)

print(f"The sum of the IDs of possible games {possible_game}")


#-----------------------------------#
#            PART 2                 #
#-----------------------------------#

possible_game = 0

with open("Data.txt", "r") as file:
  for lines in file:
    id_game, record = lines.split(": ")
    _, ID = id_game.split()
    game = True
    max_red, max_green, max_blue = 1, 1, 1
    for set_of_cubes in record.split("; "):
      for cube in set_of_cubes.split(", "):
        value, color = cube.split()

        if "red" in color and int(value) > max_red:
          max_red = int(value)
        if "green" in color and int(value) > max_green:
          max_green = int(value)
        if "blue" in color and int(value) > max_blue:
          max_blue = int(value)

    if game:
      possible_game += (max_red * max_green * max_blue)

print(f"The power of a set of cubes is equal {possible_game}")


  