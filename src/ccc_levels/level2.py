from ccc_levels.abstract_level import AbstractLevel

class Level2(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(2)
        
    # ----- methods: -----
    
    def solve_singular(self, file: int) -> None:
        input_list = self.file_access.read_file(file)
        
        output_list = list()
        
        num_path = int(input_list[0])
        
        for i in range(1, num_path + 1):
            w = 0
            d = 0
            s = 0
            a = 0
            
            for each in input_list[i]:
                match each:
                    case 'W':
                        w += 1
                    case 'D':
                        d += 1
                    case 'S':
                        s += 1
                    case 'A':
                        a += 1
                    case _:
                        raise Exception('Something went wrong')
                
            output_list.append(str(w) + ' ' + str(d) + ' ' + str(s) + ' ' + str(a))
        
        self.file_access.save_file(file, output_list)
        return None