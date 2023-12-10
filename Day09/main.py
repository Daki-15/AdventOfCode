def extrapolateP1(array):
    if all([val == 0 for val in array]):
        return 0
    deltas = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolateP1(deltas)
    return array[-1] + diff

def extrapolateP2(array):
    if all([val == 0 for val in array]):
        return 0
    deltas = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolateP2(deltas)
    return array[0] - diff 

resP1 = 0
resP2 = 0

with open("Data.txt", "r") as file:
    datas = file.read().strip().split("\n")
    datas = [list(map(int, data.split(" "))) for data in datas]

for i in range(len(datas)):
    resP1 += extrapolateP1(datas[i])
    resP2 += extrapolateP2(datas[i])

print(f"P1: What is the sum of these extrapolated values? {resP1}")
print(f"P2: What is the sum of these extrapolated values? {resP2}")