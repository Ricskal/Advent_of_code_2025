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

def verify_ids(id_list):
    score = 0
    for id in id_list:
        if len(id) % 2 != 0: # Uneven ID's are automatic valid
            # print(f'Valid id: {id}') # debug
            continue
        else: 
            id_middle = len(id) / 2
            id_middle = int(id_middle)
            id_part_1, id_part_2 = id[:id_middle], id[id_middle:] 
            id_part_1, id_part_2 = int(id_part_1), int(id_part_2) 
            if id_part_2 / id_part_1 == 1:
                # print(f'Invalid id: {id}') # debug
                score += int(id)
            else: 
                # print(f'Valid id: {id}') # debug
                continue
    return score
    
## Main method ##
if __name__ == "__main__":
    file_paths = get_input_files()
    # print(file_paths) #debug
    file_path = file_paths['input']
    # file_path = file_paths['inputTest'] #debug
    print(file_path) 
    parsed_file = parse_input_file(file_path)
    print(parsed_file)
    id_list = generate_ids(parsed_file)
    score = verify_ids(id_list)
    print(score)
    