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
    battery_bank_dict_list = []
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
        battery_enumerate_list = list(enumerate(line))
        for index_and_battery in battery_enumerate_list:
            battery_index_list = []
            index = index_and_battery[0]
            number = index_and_battery[1]
            if number not in battery_bank_dict.keys():
                battery_bank_dict[number] = battery_index_list
            battery_index_list = battery_bank_dict[number]
            battery_index_list.append(index)
            battery_bank_dict[number] = battery_index_list
        battery_bank_dict_list.append(battery_bank_dict)
    return battery_bank_dict_list

def determine_joltage(battery_bank_dict_list):
    score = 0
    found_first_number = False
    for battery_bank_dict in battery_bank_dict_list:
        max_index = max(max(values) for values in battery_bank_dict.values())
        number = 9
        while number <= 9:
            if number in battery_bank_dict.keys():
                if not found_first_number and battery_bank_dict[number][0] != max_index:
                    first_number = number
                    found_first_number = True
                    last_number_highest_index = min(battery_bank_dict[first_number])
                    number = 10
                elif found_first_number and max(battery_bank_dict[number]) > last_number_highest_index:
                    second_number = number
                    found_first_number = False
                    break
            number -= 1
        score += int(str(first_number) + str(second_number))
    return score

## Main method ##
if __name__ == "__main__":
    file_paths = get_input_files()
    # print(file_paths) #debug
    file_path = file_paths['input']
    # file_path = file_paths['inputTest'] #debug
    # print(file_path) 
    battery_bank_dict_list = parse_input_file(file_path)
    # print(battery_bank_dict_list)
    # print(parsed_file) 
    score = determine_joltage(battery_bank_dict_list)
    print(score)
    
    # 26454 too high
    # 17195 too low
    17196
    