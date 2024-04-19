from ccc_levels.abstract_level import AbstractLevel
from ccc_pathfinding.sq_cell import GridCell
from ccc_pathfinding.sq_astar import GridAStar
from ccc_pathfinding.cell_tags import CellTags

class Level3(AbstractLevel):
    
    # ----- constructor: -----
    
    def __init__(self) -> None:
        super().__init__(3)
        
    # ----- methods: -----
    
    def solve_singular(self, file: int) -> None:
        input_list = self.file_access.read_file(file)
        
        output_list = list()
        
        num_lawns = int(input_list[0])
        current_line = 1
        
        for i in range(num_lawns):
            size_str = input_list[current_line].split(' ')
            current_line += 1;
            size = list()
            for j in range(len(size_str)):
                size.append(int(size_str[j]))
            
            lawn = GridAStar()
            rows = list()
            for j in range(current_line, current_line + size[1]):
                rows.append(input_list[j])
                current_line += 1
            
            lawn.parseFromList(rows)
            
            path = input_list[current_line]
            current_line += 1
        
        
            print(lawn.get_cell_coord(0, 2).is_passable())
        
            current_x = 0
            current_y = 0
            
            valitity = True
            
            for each in path:
                match each:
                    case 'W':
                        current_x += 1
                    case 'D':
                        current_y += 1
                    case 'S':
                        current_x -= 1
                    case 'A':
                        current_y -= 1
                    case _:
                        raise Exception('Something went wrong')

                if not lawn.get_cell_coord(current_x, current_y).is_passable():
                    valitity = False
                    print('Lawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
            
            if valitity:
                output_list.append('VALID')
            else:
                output_list.append('INVALID')
        
        self.file_access.save_file(file, output_list)
        return None