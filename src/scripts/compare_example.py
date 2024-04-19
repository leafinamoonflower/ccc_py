import sys

from ccc_controller.find_level import find_level
from ccc_levels.abstract_level import AbstractLevel

def main():
    arg_list = sys.argv[1:]
    if len(arg_list) != 1:
        print('Incorrect amount of arguments given. Use: \'python src/scripts/prepare_folders.py <LEVEL>\'')
        
    level: AbstractLevel = find_level(int(arg_list[0]))
    result = level.file_access.compare_example()
    print(result)

if __name__ == '__main__':
    main()