"""
def load_input(file_path):
    with open(file_path, "r") as file:
        instruction, *elements = file.read().strip().split("\n\n")
        elements = elements[0].split("\n")
        elements_dic = {key: val for key, val in [element.split(" = ") for element in elements]}

    for key, val in elements_dic.items():
        val1, val2 = val.strip("()").split(",")
        elements_dic[key] = (val1.strip(), val2.strip())
    return instruction, elements_dic
"""
def load_input(file_path):
    with open(file_path, "r") as file:
        instruction, *elements = map(str.strip, file.read().split("\n\n"))
        elements_dic = dict(element.split(" = ") for element in elements[0].split("\n"))

    elements_dic = {key: tuple(map(str.strip, val.strip("()").split(","))) for key, val in elements_dic.items()}
    
    return instruction, elements_dic

def zzz(val, my_dict):
	return list(my_dict.keys()) [list(my_dict.values()).index(val)]

def required_steps(instruction, elements_dic):
    idx, count = 0, 0
    instruction += "//"
    element = elements_dic.get(start)

    while instruction[idx] != "//":
        if zzz(element, elements_dic) == "ZZZ":
            return count
        
        if instruction[idx] == "/":
            idx = 0
        else:
            element = elements.get(element[0]) if instruction[idx] == "L" else elements.get(element[1])
            idx , count = idx + 1, count + 1

start = "AAA"
instruction, elements = load_input("Data.txt")
print(required_steps(instruction, elements))