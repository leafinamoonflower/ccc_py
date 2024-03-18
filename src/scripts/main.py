from ccc_constants.constants import Constants
from ccc_controller.file_access import FileAccess

import sys


def main():
    arg_list = sys.argv[1:]
    if len(arg_list) > 0:
        level = arg_list[0]
        
        file_access = FileAccess(int(level))
        list = file_access.read_all_files()
        
        for each in list:
            print(each)
        
        

if __name__ == '__main__':
    main()