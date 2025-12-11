# Part One

def create_id_list(id_range_start : int, id_range_end : int) -> list:
    id_list = []
    for id in range(id_range_start, id_range_end+1):
        id_list.append(str(id))
    return id_list

def invalid_ids_1(id_list : list = []) -> list:
    invalid_ids = []
    for id in id_list:
        for sub_id in range(1, int(len(id)/2)+1):
            check = id[:sub_id]
            if(id.replace(check, "", 2) == ""):
                invalid_ids.append(int(id))
                break
    return invalid_ids
    
def get_all_invalid_ids_1(id_string : str) -> list:
    all_invalid_ids = []
    id_ranges = id_string.split(',')
    for range in id_ranges:
        id_list = create_id_list(int(range.split('-')[0]), int(range.split('-')[1]))
        all_invalid_ids.extend(invalid_ids_1(id_list))
    return all_invalid_ids
        
test1 = "11-22"
test2 = "11-22,95-115"

task_example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

print(get_all_invalid_ids(task))
print(sum(get_all_invalid_ids(task)))

task ="9595822750-9596086139,1957-2424,88663-137581,48152-65638,12354817-12385558,435647-489419,518494-609540,2459-3699,646671-688518,195-245,295420-352048,346-514,8686839668-8686892985,51798991-51835611,8766267-8977105,2-17,967351-995831,6184891-6331321,6161577722-6161678622,912862710-913019953,6550936-6625232,4767634976-4767662856,2122995-2257010,1194-1754,779-1160,22-38,4961-6948,39-53,102-120,169741-245433,92902394-92956787,531-721,64-101,15596-20965,774184-943987,8395-11781,30178-47948,94338815-94398813"

print(sum(get_all_invalid_ids_1(task_1)))

# part Two

def invalid_ids_2(id_list : list = []) -> list:
    invalid_ids = []
    for id in id_list:
        for sub_id in range(1, int(len(id)/2)+1):
            check = id[:sub_id]
            # at least 2, so 3, 4 etc. could be as well 
            if(id.replace(check, "", len(id)) == ""):
                invalid_ids.append(int(id))
    return invalid_ids
    
def get_all_invalid_ids_2(id_string : str) -> list:
    all_invalid_ids = []
    id_ranges = id_string.split(',')
    for range in id_ranges:
        id_list = create_id_list(int(range.split('-')[0]), int(range.split('-')[1]))
        all_invalid_ids.extend(invalid_ids_2(id_list))
    return list(set(all_invalid_ids))
        

print(get_all_invalid_ids_2(task_example))

print(sum(get_all_invalid_ids_2(task_example)))

print(sum(get_all_invalid_ids_2(task)))