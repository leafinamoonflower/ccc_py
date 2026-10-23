import sys
import os
from zipfile import ZipFile
from ccc_constants.constants import Constants

def main():
    arg_list = sys.argv[1:]
    
    if len(arg_list) != 2:
        print('Incorrect amount of arguments given. Use: \'just extract <LEVEL> <PATH>\'')
        return

    level = int(arg_list[0])
    if type(level) is not int:
        print('Incorrect Level Type given. Use: \'just extract <LEVEL> <PATH>\'')
        return

    filename = arg_list[1]
    if type(filename) is not str:
        print('Incorrect Path given. Use: \'just extract <LEVEL> <PATH>\'')

    if filename[0] == '~':
        filename = os.path.expanduser(arg_list[1])

    input_dir = Constants.DIRECTORY + 'level' + str(level) + '/input/'
    docs_dir = Constants.DIRECTORY + 'docs/'

    with ZipFile(filename, mode="r") as archive:
        for file in archive.namelist():
            if file.startswith('in'):
                archive.extract(file, path=input_dir)
            # elif file.endswith('.pdf'):
            #     archive.extract(file, path=docs_dir)
            else:
                archive.extract(file, path=docs_dir)
        
if __name__ == '__main__':
    main()
