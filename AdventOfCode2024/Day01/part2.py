def read_data(path):
    right_count = {}
    left = []
    res = 0

    with open(path, "r") as data:
        for line in data:
            l, r = map(int, line.strip().split())

            left.append(l)

            if r in right_count:
                right_count[r] += 1
            else:
                right_count[r] = 1

        for l in left:
            res += l * right_count.get(l, 0)

    print(res)


read_data("./input.txt")