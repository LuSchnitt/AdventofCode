
def AoC_5_1(filename : str) -> int:
    all_range = []
    fresh_counter = 0
    mode = 1
    for line in open("./" + filename, "rt"):
        if line == "\n":
            if(mode == 2):
                break
            mode = 2
            continue
        if mode == 1:
            number_range = line.split("-")
            number_range[1] = number_range[1].removesuffix("\n")
            all_range.append(number_range)
        elif mode == 2:
            check = False
            id = int(line)
            for range in all_range:
                if(id >= int(range[0]) and id <= int(range[1])):
                    check = True
                    break
            if(check == True):
                fresh_counter += 1
    return fresh_counter


file_name = "AoC_5_Input.txt"

print(AoC_5_1(file_name))