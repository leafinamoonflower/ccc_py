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
            up_cur = 0
            right_cur = 0
            
            up = 0
            up_neg = 0
            right = 0
            right_neg = 0
            
            for each in input_list[i]:
                match each:
                    case 'W':
                        up_cur += 1
                        if up_cur > up:
                            up = up_cur
                    case 'D':
                        right_cur += 1
                        if right_cur > right:
                            right = right_cur
                    case 'S':
                        up_cur -= 1
                        if up_cur < up_neg:
                            up_neg = up_cur
                    case 'A':
                        right_cur -= 1
                        if right_cur < right_neg:
                            right_neg = right_cur
                    case _:
                        raise Exception('Something went wrong')
                
            output_list.append(str(right - right_neg + 1) + ' ' + str(up - up_neg + 1)) 
        
        self.file_access.save_file(file, output_list)
        return None