# Open the file "Data.txt" for reading
with open("Data.txt", "r") as file:
    # Read the contents of the file and split them into seeds and blocks
    seeds, *blocks = file.read().split("\n\n")
    # Convert seeds to a list of integers
    seeds = list(map(int, seeds.split(":")[1].split()))

# Loop through each block in the blocks
for block in blocks:
    # Initialize an empty list to store ranges in the block
    ranges = []
    
    # Iterate over each line in the block (excluding the first line)
    for line in block.splitlines()[1:]:
        # Split the line into destination, source, and range; convert to integers
        destination, source, rng = list(map(int, line.split()))
        # Append a tuple of (destination, source, range) to the ranges list
        ranges.append((destination, source, rng))

    # Initialize an empty list to store results for each seed in seeds
    res = []
    
    # Iterate over each seed in seeds
    for seed in seeds:
        # Iterate over each range in ranges
        for destination, source, rng in ranges:
            # Check if seed falls within the source and source + range
            if source <= seed < source + rng:
                # Calculate the result and append to res
                res.append(seed - source + destination)
                # Break out of the inner loop since we found a match
                break
        else:
            # If no match is found in the inner loop, append the seed as is to res
            res.append(seed)

    # Update seeds with the results from res for the next iteration
    seeds = res
# Print the minimum value in the final seeds list
print(min(seeds))
