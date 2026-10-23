from ccc_constants.constants import Constants
import os

class FileAccess:
    
    def __init__(self, level: int) -> None:
        if level > 0:
            self._level = level
            self._directory = Constants.DIRECTORY + 'level' + str(self._level) + '/'
        else:
            raise Exception('FileAccess: Level must be greater than 0!')
    
    
    def prepare_folders(self) -> None:
        input_dir = self._directory + 'input/'
        output_dir = self._directory + 'output/'
        docs_dir = Constants.DIRECTORY + 'docs/'
        os.makedirs(input_dir)
        os.makedirs(output_dir)
        if not os.path.exists(docs_dir):
            os.makedirs(docs_dir)
     
        
    def read_file(self, file: int) -> list:
        if file == 0:
            path = self._directory + 'input/level' + str(self._level) + '_example.in'
        elif 0 < file and file < 6:
            path = self._directory + 'input/level' + str(self._level) + '_' + str(file) + '.in'
        else:
            raise Exception("Wrong File-Number")
        
        if not os.path.exists(path):
            raise FileNotFoundError('File ' + path + ' was not found.')
        open_file = open(path, 'r')
        lines = list()
        for each in open_file:
            lines.append(each.strip())
        return lines
        
    
    def save_file(self, file: int, input: list) -> None:
        if file == 0:
            path = self._directory + 'output/level' + str(self._level) + '_example.out'
        elif 0 < file and file < 6:
            path = self._directory + 'output/level' + str(self._level) + '_' + str(file) + '.out'
        else:
            raise Exception("Wrong File-Number")
        
        if os.path.exists(path):
            os.remove(path)
        open_file = open(path, 'a')
        max_length = len(input)
        for i in range(max_length - 1):
            open_file.write(input[i] + '\n')
        open_file.write(input[max_length - 1])
