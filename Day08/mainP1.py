def load_input(file_path):
    with open(file_path, "r") as file:
        instruction, *elements = map(str.strip, file.read().split("\n\n"))
        elements_dic = dict(element.split(" = ") for element in elements[0].split("\n"))

    elements_dic = {key: tuple(map(str.strip, val.strip("()").split(","))) for key, val in elements_dic.items()}
    
    return instruction, elements_dic

count = 0
current = "AAA"

def required_steps(steps, elements_dic):
    current = "AAA"
    count = 0
    
    while current != "ZZZ":
        count += 1
        current = elements_dic[current][0 if steps[0] == 'L' else 1]
        steps = steps[1:] + steps[0]
    return count

instruction, elements = load_input("Data.txt")
print(required_steps(instruction, elements))