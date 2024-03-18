from levels.abstract_level import AbstractLevel

class Level1(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(1)
        
    # ----- methods: -----
    
    def solve_example(self) -> None:
        input_list = self.file_access.read_example_file
        
        print('solve_example() was not implemented yet.')
        return None
    
    def solve_singular(self, file: int) -> None:
        input_list = self.file_access.read_singular_file(file)
        self.file_access.save_singular_file(file, input_list)
        
        print('solve_singular() was not implemented yet.')
        return None