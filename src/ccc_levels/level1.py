from ccc_levels.abstract_level import AbstractLevel

class Level1(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(1)
        
    # ----- methods: -----
    
    def solve_singular(self, file: str) -> None:
        input = self.file_access.read_file(file)
        out = []

        line = 0

        first = input[line]
        line += 1
        
        self.file_access.save_file(file, out)
        return None
