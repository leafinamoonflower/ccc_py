import sys

from ccc_controller.find_level import find_level
from ccc_levels.abstract_level import AbstractLevel
from ccc_pathfinding.sq_astar import GridAStar

def main():
    arg_list = sys.argv[1:]
    
    if len(arg_list) != 1:
        print('Incorrect amount of arguments given. Use: \'just solve_singular <LEVEL> <FILE>\'')
        return

    print(type(arg_list[0]))
    
    #level: AbstractLevel = find_level(int(arg_list[0]))
    
    #else:
    #    print('Input for <FILE> was out of bounds.')

if __name__ == '__main__':
    main()
