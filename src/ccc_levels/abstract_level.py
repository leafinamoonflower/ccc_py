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
    def solve_singular(self, file: int) -> None:
        pass
    
    def solve_all(self) -> None:
        for i in range(1, 6):
            self.solve_singular(i)