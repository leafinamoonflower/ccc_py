import sys

from ccc_controller.find_level import find_level
from ccc_levels.abstract_level import AbstractLevel
from ccc_levels.level1 import Level1

def main():
    arg_list = sys.argv[1:]
    
    if len(arg_list) != 1:
        print('Incorrect amount of arguments given. Use: \'python src/scripts/solve_all.py <LEVEL>\'')
        return
    
    level: AbstractLevel = find_level(int(arg_list[0]))
    
    level.solve_all()
        
    
if __name__ == '__main__':
    main()