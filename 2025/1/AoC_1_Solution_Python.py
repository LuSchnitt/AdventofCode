def password_cracker_AoC1_1(start  : int = 50, sequence : list = None) -> int:
    z_counter = 0
    dial = start
    for instruction in sequence:
        number = int(instruction[1:])
        move = instruction[0]
        if move == "R":
            dial = (dial + number) % 100
        else:
            dial = (dial - number) % 100
        if dial == 0:
            z_counter += 1
    return z_counter

def password_cracker_AoC1_2(start  : int = 50, sequence : list = None) -> int:
    z_counter = 0
    dial = start
    for instruction in sequence:
        number = int(instruction[1:])
        move = instruction[0]
        for _ in range(number):
            if move == "R":
                dial += 1
            else:
                dial -= 1
            dial %= 100
            if(dial == 0):
                z_counter += 1
    return z_counter
                
def read_instruction_from_file(file_name : str = "AoC_1_Task_Input.txt") -> list:
    sequence_list = []
    file = open("./" + file_name, 'rt')
    for line in file:
        sequence_list.append(line.removesuffix('\n'))
    return sequence_list
        
start = 50

# Test-Cases for Task 2

# Solution = 6
test_sequence = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

# Solution = 16
test_sequence2 = ['R1000', 'L149', 'L1', 'R1', 'L2', 'R1', 'L1', 'R2', 'R99']

# Solution all 11
test_sequence3 = ['L50', 'L1000']
test_sequence4 = ['R50', 'R1000']

# Solution all 1
test_sequence5 = ['L50', 'R50']
test_sequence6 = ['L50', 'L50']
test_sequence7 = ['R50', 'L50']
test_sequence8 = ['R50', 'R50']

# Solution all 2
test_sequence9 = ['L150', 'L50']
test_sequence10 = ['L150', 'R50']
test_sequence11= ['R150', 'L50']
test_sequence12 = ['R150', 'R50']

# Solution all 3
test_sequence13 = ['L250', 'L50']
test_sequence14 = ['L250', 'R50']
test_sequence15= ['R250', 'L50']
test_sequence16 = ['R250', 'R50']

def test_AoC1_2():
    assert password_cracker_AoC1_2(start, test_sequence) == 6
    assert password_cracker_AoC1_2(start, test_sequence2) == 16
    assert password_cracker_AoC1_2(start, test_sequence3) == 11
    assert password_cracker_AoC1_2(start, test_sequence4) == 11
    assert password_cracker_AoC1_2(start, test_sequence5) == 1
    assert password_cracker_AoC1_2(start, test_sequence6) == 1
    assert password_cracker_AoC1_2(start, test_sequence7) == 1
    assert password_cracker_AoC1_2(start, test_sequence8) == 1
    assert password_cracker_AoC1_2(start, test_sequence9) == 2
    assert password_cracker_AoC1_2(start, test_sequence10) == 2
    assert password_cracker_AoC1_2(start, test_sequence11) == 2
    assert password_cracker_AoC1_2(start, test_sequence12) == 2
    assert password_cracker_AoC1_2(start, test_sequence13) == 3
    assert password_cracker_AoC1_2(start, test_sequence14) == 3
    assert password_cracker_AoC1_2(start, test_sequence15) == 3
    assert password_cracker_AoC1_2(start, test_sequence16) == 3
    
test_AoC1_2()

sequence = read_instruction_from_file()

print(password_cracker_AoC1_1(start, sequence))

print(password_cracker_AoC1_2(start, sequence))


