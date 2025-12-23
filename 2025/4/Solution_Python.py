
# Part One

import numpy as np

def read_input(file_name : str) -> np.ndarray:
    matrix_list = []
    mapper = {"@" : 1, "." : 0}
    for line in open("./" + file_name, "r"):
        tmp_list = []
        for sign in line:
            if(sign == "\n"):
                continue
            tmp_list.append(mapper[sign])
        matrix_list.append(tmp_list)
    return np.matrix(matrix_list)

def check_neighborhood(matrix : np.ndarray, index : tuple) -> bool:
    lower_row = index[0] - 1 if index[0] > 0 else 0
    upper_row = index[0] + 1
    
    lower_col = index[1] - 1 if index[1] > 0 else 0
    upper_col = index[1] + 1
     
    tmp_counter = matrix[lower_row:upper_row + 1, lower_col:upper_col + 1].sum() - 1
    #print(index)
    #print(matrix[lower_row:upper_row + 1, lower_col:upper_col + 1])
    #print(tmp_counter)
    
    if(tmp_counter < 4):
        return 1, index
    
    return 0, index
        
def find_movable_rolls_1(matrix : np.ndarray) -> int:
    counter = 0
    indexes = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            if(matrix[row, col] == 1):
                tmp_1, tmp_2 = check_neighborhood(matrix, (row, col))
                counter += tmp_1
                if(tmp_1 == 1):
                    indexes.append(tmp_2)
        
    return counter#, indexes 

filename_test = "AoC4_Test_Input.txt"

test_input = read_input(filename_test)

#print(test_input)

#print(find_movable_rolls_1(test_input))

filename_task = "AoC4_Task_Input.txt"

task_input = read_input(filename_task)

#print(find_movable_rolls_1(task_input))

# Part Two

def find_movable_rolls_2(matrix : np.ndarray) -> int:
    counter = 0
    all_indexes = []
    while True:
        tmp_indexes = []
        for row in range(matrix.shape[0]):
            for col in range(matrix.shape[1]):
                if(matrix[row, col] == 1):
                    tmp_1, tmp_2 = check_neighborhood(matrix, (row, col))
                    counter += tmp_1
                    if(tmp_1 == 1):
                        tmp_indexes.append(tmp_2)
       
        for index in tmp_indexes:
            matrix[index] = 0
        if(len(tmp_indexes) == 0):
            #print(matrix)
            break
        else:
            all_indexes.extend(tmp_indexes)
    return counter
             
print(find_movable_rolls_2(test_input))

print(find_movable_rolls_2(task_input))   