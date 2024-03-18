from abc import ABC, abstractmethod
from ccc_controller.file_access import FileAccess

class AbstractLevel(ABC):
    
    # ----- constructor: -----
    
    def __init__(self, level: int) -> None:
        self._file_access = FileAccess(level)
        
    # ----- getter and setter: -----
    
    @property
    def file_access(self):
        return self._file_access

    # ----- methods: -----
    
    @abstractmethod
    def solve_example(self) -> None:
        pass
    
    @abstractmethod
    def solve_singular(self, file: int) -> list:
        pass
    
    def solve_all(self) -> list:
        solved_list = list()
        for i in range(1, 6):
            solved_list.append(self.solve_singular(i))
        return solved_list