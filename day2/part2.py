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
    return parsed_file

## Main method ##
if __name__ == "__main__":
    file_paths = get_input_files()
    # print(file_paths) #debug
    # file_path = file_paths['input']
    file_path = file_paths['inputTest'] #debug
    print(file_path) 
    parsed_file = parse_input_file(file_path)
    print(parsed_file) 
    