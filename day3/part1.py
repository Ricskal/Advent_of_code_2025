## imports ##
import os

## variables ##
expectedTestOutputPart1 = 357
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
    parsed_file_part_1 = []
    parsed_file_part_2 = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            parsed_file_part_1.append(list(line))
    for line in parsed_file_part_1:
        new_line = []
        for char in line:
            new_line.append(int(char))
        parsed_file_part_2.append(new_line)
    for line in parsed_file_part_2:
        battery_bank_dict = {}
        battery_index_list = list(enumerate(line))
        for index_and_battery in battery_index_list:
            listy = []
            index = index_and_battery[0]
            number = index_and_battery[1]
            if number not in battery_bank_dict.keys():
                battery_bank_dict[number] = listy
            listy = battery_bank_dict[number]
            listy.append(index)
            battery_bank_dict[number] = listy
        print(battery_bank_dict)
    return parsed_file_part_2

# def determine_joltage(parsed_file):
#     for line in parsed_file:
#         for number in line:
#     return parsed_file

## Main method ##
if __name__ == "__main__":
    file_paths = get_input_files()
    # print(file_paths) #debug
    # file_path = file_paths['input']
    file_path = file_paths['inputTest'] #debug
    # print(file_path) 
    parsed_file = parse_input_file(file_path)
    # print(parsed_file) 
    # determine_joltage(parsed_file)
    