## imports ##
import os

## variables ##
expectedTestOutputPart1 = 0
expectedTestOutputPart2 = 0

## Methods ##
def get_input_files():
    current_file_path = os.path.abspath(__file__)
    curren_folder_path = os.path.dirname(current_file_path)
    file_paths = {
        'input': curren_folder_path + '\\input.txt',
        'inputTest': curren_folder_path + '\\inputTest.txt',
    }
    return file_paths

def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            parsed_file = line.split(',')
    return parsed_file

def generate_ids(parsed_file):
    id_list = []
    for id_range in parsed_file:
        start_range, end_range = id_range.split('-')
        start_range, end_range = int(start_range), int(end_range)
        for id in range(start_range, end_range + 1):
            id_list.append(str(id))
    return id_list

def verify_ids_part_1(id_list):
    part2_id_list = []
    score_1 = 0
    for id in id_list:
        if len(id) % 2 != 0: # Uneven ID's are automatic valid
            # print(f'Valid id: {id}') # debug
            part2_id_list.append(id)
            continue
        else: 
            id_middle = len(id) / 2
            id_middle = int(id_middle)
            id_part_1, id_part_2 = id[:id_middle], id[id_middle:] 
            id_part_1, id_part_2 = int(id_part_1), int(id_part_2) 
            if id_part_2 / id_part_1 == 1:
                # print(f'Invalid id: {id}') # debug
                score_1 += int(id)
            else: 
                # print(f'Valid id: {id}') # debug
                part2_id_list.append(id)
                continue
    return score_1, part2_id_list

def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            if i != number and (number / i) != 2: divisors.append(i)
    return divisors

def verify_ids_part_2(part2_id_list):
    score_2 = 0
    for id in part2_id_list:
        length_id = len(id)
        divisors_list = find_divisors(length_id)
        for divisor in divisors_list:
            invalid_id_bool = True
            block_n1 = '-1'
            start_block = 0
            end_block = 0
            for x in range(0, int(length_id / divisor)):
                start_block = x * divisor
                end_block = end_block + divisor
                block_n = id[start_block:end_block]
                if x != 0 and block_n != block_n1:
                    invalid_id_bool = False
                    break
                block_n1 = block_n
            if invalid_id_bool:
                score_2 += int(id)
                break
    return score_2
    
## Main method ##
if __name__ == "__main__":
    file_paths = get_input_files()
    file_path = file_paths['input'] #prod
    # file_path = file_paths['inputTest'] #debug?
    parsed_file = parse_input_file(file_path)
    id_list = generate_ids(parsed_file)
    score_1, part2_id_list = verify_ids_part_1(id_list)
    print(f'Score part 1: {score_1}')
    score_2 = verify_ids_part_2(part2_id_list)
    print(f'Score part 2: {score_2}')
    print(f'Score part 1 + 2: {score_1 + score_2}')