# Part one

def read_input(filename : str) -> list:
    bank_list = []
    file = open("./" + filename, 'rt')
    for line in file:
        bank_list.append(line.removesuffix("\n"))
    return bank_list

def number_to_list(number : str) -> list:
    number_list = []
    number_str = str(number)
    for digit in number_str:
        number_list.append(int(digit))
    return number_list

def get_max_joltage(banks : list) -> int:
    joltage_output = 0
    first_jol = 0
    second_jol = 0
    first_jol_index = 0
    second_jol_index = 0
    for bank in banks:
         bank_list = number_to_list(bank)
         first_jol = max(bank_list)
         first_jol_index = bank_list.index(first_jol)
         if(first_jol_index == len(bank_list)-1):
            second_jol = max(bank_list[0:first_jol_index])
            second_jol_index = bank_list[0:first_jol_index].index(second_jol)
         elif(first_jol_index == 0):
            second_jol = max(bank_list[1:])
            second_jol_index = bank_list[1:].index(second_jol) + 1
         else:
            second_jol = max(bank_list[first_jol_index+1:])
            second_jol_index = bank_list[first_jol_index+1:].index(second_jol) + first_jol_index
         if(first_jol_index > second_jol_index):
            first_jol, second_jol = second_jol, first_jol
         joltage_output += int(str(first_jol) + str(second_jol))
    return joltage_output

test_input = ["987654321111111", "811111111111119" ,"234234234234278", "818181911112111"]

print(get_max_joltage(test_input))

filename = "Task_Input.txt"

task_input = read_input(filename)

#print(get_max_joltage(task_input))


# Part two

def get_max_joltage_2(banks : list, number_batteries : int) -> int:
    joltage_output = 0
    for bank in banks:
         bank_list = number_to_list(bank)
         jol_values = []
         last_index = 0
         num_digits = number_batteries
         while num_digits > 0:
            max_index = len(bank_list) - num_digits + 1
            jol_values.append(max(bank_list[last_index:max_index]))
            last_index += bank_list[last_index:max_index].index(jol_values[-1]) + 1
            num_digits -= 1
         jol_string = ""
         for jol in jol_values:
            jol_string += str(jol)
         print(jol_string)
         joltage_output += int(jol_string)
    return joltage_output

print(get_max_joltage_2(task_input , 12))