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
        os.makedirs(input_dir)
        os.makedirs(output_dir)
    
    
    def _read_file(self, path: str) -> list:
        if not os.path.exists(path):
            raise FileNotFoundError('File ' + path + ' was not found.')
        open_file = open(path, 'r')
        lines = list()
        for each in open_file:
            lines.append(each.strip())
        return lines
    
        
    def read_example_file(self) -> list:
        path = self._directory + 'input/level' + str(self._level) + '_example.in'
        return self._read_file(path)
     
        
    def read_singular_file(self, file: int) -> list:
        path = self._directory + 'input/level' + str(self._level) + '_' + str(file) + '.in'
        return self._read_file(path)
    
    
    def _save_file(self, path: str, input: list) -> None:
        open_file = open(path, 'a')
        for each in input:
            open_file.write(each + '\n')
            
    
    def save_example_file(self, input: list) -> None:
        path = self._directory + 'output/level' + str(self._level) + '_example.out'
        self._save_file(path, input)
        
    
    def save_singular_file(self, file: int, input: list) -> None:
        path = self._directory + 'output/level' + str(self._level) + '_' + str(file) + '.out'
        self._save_file(path, input)