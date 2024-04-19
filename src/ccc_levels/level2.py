from ccc_levels.abstract_level import AbstractLevel

class Level2(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(2)
        
    # ----- methods: -----
    
    def solve_singular(self, file: int) -> None:
        input_list = self.file_access.read_file(file)
        
        num_cur = int(input_list[0])
        num_val = int(input_list[1])
        num_amount = int(input_list[2])
        output_list = list()
        for i in range(3, num_cur * 2 + 3, 2):
            val_list = list()
            temp = list(input_list[i].split(' '))
            for j in temp:
                val_list.append(int(j))
                
            tar_list = list()
            temp = list(input_list[i + 1].split(' '))
            for j in temp:
                tar_list.append(int(j))
                
            for j in tar_list:
                found_target = False
                dict_map = {}
                
                n = len(val_list)
                for t in range(n):
                    for s in range(t, n):
                        if val_list[t] + val_list[s] == j and not found_target:
                            print(str(val_list[t]) + ' ' + str(val_list[s]) + ' ' + str(j))
                            output_list.append(str(val_list[t]) + ' ' + str(val_list[s]))
                            found_target = True
                            break
        
        # TODO: stub
        
        self.file_access.save_file(file, output_list)
        
        print('solve_singular() was not implemented yet.')
        return None