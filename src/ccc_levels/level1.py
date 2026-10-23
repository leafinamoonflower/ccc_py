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

        cases = int(input[line])
        line += 1

        for i in range(cases):
            radius = int(input[line])
            hex_out = []

            middle = '*-'
            for j in range(radius * 2 - 1):
                middle += 'O-'
            middle += '*'
            hex_out.append(middle)

            next = middle
            for j in range(radius - 1):
                next = next.replace('O-', '', 1)
                next = "".join(['-', next, '-'])
                hex_out.insert(0,next)
                hex_out.append(next)
            next = next.replace('O-', '', 1)
            next = "".join(['-', next, '-'])
            next = next.replace('O', '*')
            hex_out.insert(0, next)
            hex_out.append(next)

            for hex_line in hex_out:
                out.append(hex_line)
            
            if i != cases - 1:
                out.append('')
            line += 1
        self.file_access.save_file(file, out)
        return None
