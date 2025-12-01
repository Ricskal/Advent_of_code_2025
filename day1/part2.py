## imports ##
import os

## variables ##
expectedTestOutputPart1 = 3
# expectedTestOutputPart2 = 0

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
    file_list = []
    with open(file_path, 'r') as file:
        for line in file:
            file_list.append(line.strip())
    return file_list

def turn_dail(parsed_file):
    score = 0
    previous_position = 1
    current_position = 50
    min_position = 0
    max_position = 99
    number_of_clicks_list = []
    for direction in parsed_file:
        left_or_right = direction[0]
        number_of_clicks = direction[1:]
        number_of_clicks_list.append(int(number_of_clicks[-2:])) 
        number_of_clicks = int(number_of_clicks)
        while number_of_clicks > 100:
                number_of_clicks_list.append(100)
                number_of_clicks -= 100
        
        for clicks in number_of_clicks_list:
            if left_or_right == 'R': 
                current_position += clicks
                if current_position > max_position: 
                    current_position = current_position - 100
                    if current_position != 0 and previous_position != 0: score += 1
            if left_or_right == 'L': 
                current_position -= clicks
                if current_position < min_position: 
                    current_position = current_position + 100
                    if current_position != 0 and previous_position != 0: score += 1
                    
            print(current_position) #debug
            previous_position = current_position
            if current_position == 0: score += 1
        number_of_clicks_list = []
    return score        

## Main method ##
if __name__ == "__main__":
    file_paths = get_input_files()
    # print(file_paths) #debug
    file_path = file_paths['input'] #prod
    # file_path = file_paths['inputTest'] #debug
    # print(file_path) #debug
    parsed_file = parse_input_file(file_path)
    # print(parsed_file) #debug
    score = turn_dail(parsed_file)
    print(f'De score is: {score}')