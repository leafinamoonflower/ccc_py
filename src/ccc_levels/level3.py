from ccc_levels.abstract_level import AbstractLevel

class Level3(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(3)
        
    # ----- methods: -----
    
    def solve_singular(self, file: int) -> None:
        input_list = self.file_access.read_file(file)
        
        num_cur = int(input_list[0])
        num_val = int(input_list[1])
        output_list = list()
        for i in range(2, num_cur + 2):
            val_list = list()
            temp = list(input_list[i].split(' '))
            for j in temp:
                val_list.append(int(j))
            val_list.reverse()
            n = len(val_list)
              
                
            for j in range(100):
                dict_map = {}
                for each in val_list:
                    dict_map[each] = 0  
                
                target = j + 1
                current = 0
                
                current_temp = 0
                dict_amount = {}
                for each in range(n):
                    dict_amount[each] = 0 
                max_coins = {}
                for each in range(n):
                    max_coins[each] = 0
                use_range = 0
                
                while current_temp < target:
                    for t in range(n - 1):
                        for s in range(n - t):
                            if current_temp + val_list[s] <= target:
                                current_temp += val_list[s]
                                max_coins[t] += 1
                                break
                    
                    for each in dict_amount:
                        if dict_amount[each] < max_coins[each]:
                            use_range = n - each
                            
                while current < target:
                    for t in range(use_range):
                        if current + val_list[t] <= target:
                            current += val_list[t]
                            dict_map[val_list[t]] += 1
                            break
                
                if current == target:
                    temp = val_list
                    temp.reverse
                    output_str = str()
                    for each in val_list:
                        if not dict_map[each] == 0:
                            output_str += str(dict_map[each]) + 'x' + str(each) + ' '
                    output_str = output_str.strip()
                    print(output_str)
                    output_list.append(output_str)
                elif current > 100:
                    print(current)
                    raise Exception("ERROR, over 100!")  
        
        self.file_access.save_file(file, output_list)
        return None