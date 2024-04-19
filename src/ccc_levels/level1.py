from ccc_levels.abstract_level import AbstractLevel

class Level1(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(1)
        
    # ----- methods: -----
    
    def solve_singular(self, file: int) -> None:
        input_list = self.file_access.read_file(file)
        
        num_cur = int(input_list[0])
        num_val = int(input_list[1])
        output_list = list()
        for i in range(2, 2 + num_cur):
            val_list = list()
            temp = list(input_list[i].split(' '))
            for j in temp:
                val_list.append(int(j))

            for j in range(1, num_val + 1):
                if not val_list[j - 1] == j:
                    output_list.append(j)
                    print(j)
                    break
        
        # TODO: stub
        
        self.file_access.save_file(file, output_list)
        
        print('solve_singular() was not implemented yet.')
        return None