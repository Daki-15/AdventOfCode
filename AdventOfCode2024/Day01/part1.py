def read_data(path):
    with open(path, "r") as data:
        left = []
        right = []

        for line in data:
            l, r = map(int, line.strip().split())

            left.append(l)
            right.append(r)

    left.sort()
    right.sort()

    res = sum(abs(l - r) for l, r in zip(left, right))

    print(res)

read_data("./input.txt")