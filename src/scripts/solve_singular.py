import sys

from ccc_controller.find_level import find_level
from ccc_levels.abstract_level import AbstractLevel

def main():
    arg_list = sys.argv[1:]
    
    if len(arg_list) != 2:
        print('Incorrect amount of arguments given. Use: \'just solve_singular <LEVEL> <FILE>\'')
        return
    
    level: AbstractLevel = find_level(int(arg_list[0]))
    
    file: str = arg_list[1]
    
    level.solve_singular(file)
        
if __name__ == '__main__':
    main()
