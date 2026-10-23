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
        if not os.path.exists(input_dir):
            os.makedirs(input_dir)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        if not os.path.exists(docs_dir):
            os.makedirs(docs_dir)     
        
    def read_file(self, file: str) -> list:
        if not os.path.exists(file):
            raise FileNotFoundError('File ' + file + ' was not found.')
        open_file = open(file, 'r')
        lines = list()
        for each in open_file:
            lines.append(each.strip())
        return lines
        
    
    def save_file(self, file: str, input: list) -> None:
        path = self._directory + 'output/' + file.split('/')[-1].replace('in', 'out')
        if os.path.exists(path):
            os.remove(path)
        open_file = open(path, 'a')
        max_length = len(input)
        for i in range(max_length - 1):
            open_file.write(input[i] + '\n')
        open_file.write(input[max_length - 1])
