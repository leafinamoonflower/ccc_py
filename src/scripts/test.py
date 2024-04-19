import sys

from ccc_controller.find_level import find_level
from ccc_levels.abstract_level import AbstractLevel
from ccc_pathfinding.sq_astar import GridAStar

def main():
    arg_list = sys.argv[1:]
    
    if len(arg_list) != 2:
        print('Incorrect amount of arguments given. Use: \'just solve_singular <LEVEL> <FILE>\'')
        return
    
    level: AbstractLevel = find_level(int(arg_list[0]))
    
    file: int = int(arg_list[1])
    
    if 0 <= file and file < 6:
        input = level.file_access.read_file(1)
        astar = GridAStar()
        astar.parseFromList(input)
        
    else:
        print('Input for <FILE> was out of bounds.')

if __name__ == '__main__':
    main()