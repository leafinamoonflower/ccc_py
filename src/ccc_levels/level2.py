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
        for i in range(3, 3 + num_cur, 1):
            val_list = list()
            temp = list(input_list[i].split(' '))
            for j in temp:
                val_list.append(int(j))
                
            tar_list = list()
            temp = list(input_list[i + 1].split(' '))
            for j in temp:
                tar_list.append(int(j))

            for j in tar_list:
                dict_map = {}
                for t in range(len(val_list)):
                    dict_map[t] = val_list[t]
                    
                
                for t in range(len(val_list)):
                    complement = j - dict_map[t]
                    if complement in dict_map and dict_map[complement] != val_list[t]:
                        output_list.append(str(t) + ' ' + str(dict_map[complement]))
                        print(str(j) + ' ' + str(t) + ' ' + str(dict_map[complement]))
                        break
        
        # TODO: stub
        
        self.file_access.save_file(file, output_list)
        
        print('solve_singular() was not implemented yet.')
        return None