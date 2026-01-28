import numpy as np

def AoC_6_1(filename : str) -> int:
    number_list = []
    for line in open("./" + filename, "rt"):
        line_split = line.removesuffix("\n").split()
        if(line_split[0] not in ["*", "+"]):
            number_list.append(line_split)
        else:
            op_list = line_split
    np_array = np.array(number_list,  dtype=int)
    np_array = np_array.T
    addup = 0
    for row, op in zip(range(np_array.shape[0]), op_list):
        if(op == '*'):
            addup += np.prod(np_array[row, :])
        else:
            addup += sum(np_array[row, :])
    return addup

test_file = "AoC_6_Test_Input.txt"
task_file = "AoC_6_Task_Input.txt"

print(AoC_6_1(task_file))

def Cephalopod_math_mapping(array, op) -> int:
    pass
    #todo Continue