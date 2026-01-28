
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


def AoC_5_2(filename: str):
    all_range = []
    with open(filename, "rt") as f:
        for line in f:
            if line == "\n":
                break
            a, b = line.strip().split("-")
            all_range.append([int(a), int(b)])

    all_range.sort(key=lambda r: (r[0], r[1]))

    merged = []
    cur_min, cur_max = all_range[0]

    for start, end in all_range[1:]:
        if start <= cur_max + 1:               
            cur_max = max(cur_max, end)       
        else:
            merged.append([cur_min, cur_max])
            cur_min, cur_max = start, end

    merged.append([cur_min, cur_max])

    fresh_ids = sum(b - a + 1 for a, b in merged)
    return fresh_ids

file_name = "AoC_5_Task_Input.txt"
test_filename = "AoC_5_Test_Input.txt"

#print(AoC_5_1(file_name))
print(AoC_5_2(file_name))
