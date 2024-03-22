import sys

from ccc_controller.find_level import find_level
from levels.abstract_level import AbstractLevel

def main():
    arg_list = sys.argv[1:]
    
    if len(arg_list) != 2:
        print('Incorrect amount of arguments given. Use: \'just solve_singular <LEVEL> <FILE>\'')
        return
    
    level: AbstractLevel = find_level(int(arg_list[0]))
    
    file: int = int(arg_list[1])
    
    if 0 <= file and file < 6:
        level.solve_singular(file)
    else:
        print('Input for <FILE> was out of bounds.')
        
        
if __name__ == '__main__':
    main()