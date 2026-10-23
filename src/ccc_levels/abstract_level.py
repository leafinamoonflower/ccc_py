import os
from abc import ABC, abstractmethod
from ccc_controller.file_access import FileAccess
from ccc_constants.constants import Constants

class AbstractLevel(ABC):
    
    # ----- constructor: -----
    
    def __init__(self, level: int) -> None:
        self._level = level
        self._file_access = FileAccess(level)
        
    # ----- getter and setter: -----
    
    @property
    def file_access(self):
        return self._file_access

    # ----- methods: -----
    
    @abstractmethod
    def solve_singular(self, file: str) -> None:
        pass
    
    def solve_all(self) -> None:
        level_dir = Constants.DIRECTORY + 'level' + str(self._level) + '/'
        files = os.listdir(level_dir)
        files = [file for file in files if os.path.isfile(level_dir + '/' + file)]
        for file in files:
            if file.startswith('in'):
                self.solve_singular(level_dir + '/' + file)
