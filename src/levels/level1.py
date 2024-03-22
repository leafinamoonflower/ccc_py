from levels.abstract_level import AbstractLevel

class Level1(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(1)
        
    # ----- methods: -----
    
    def solve_singular(self, file: int) -> None:
        input_list = self.file_access.read_file(file)
        self.file_access.save_file(file, input_list)
        
        print('solve_singular() was not implemented yet.')
        return None