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
                # [0] = x, [1] = y
            
            rows = list()
            for j in range(current_line, current_line + size[1]):
                rows.append(input_list[j])
                current_line += 1
            
            path = input_list[current_line]
            print(path)
            current_line += 1
            
            up_cur = 0
            right_cur = 0
            
            down = 0
            up = 0
            left = 0
            right = 0
            
            for each in path:
                match each:
                    case 'W':
                        up_cur -= 1
                        if up_cur < down:
                            down = up_cur
                    case 'D':
                        right_cur += 1
                        if right_cur > right:
                            right = right_cur
                    case 'S':
                        up_cur += 1
                        if up_cur > up:
                            up = up_cur
                    case 'A':
                        right_cur -= 1
                        if right_cur < left:
                            left = right_cur
                    case _:
                        raise Exception('Something went wrong')
                
            print('up: ' + str(up) + ' down: ' + str(down) + ' left: ' + str(left) + ' right: ' + str(right))    
            print('size_x: ' + str(size[0]) + ' size_y: ' + str(size[1]))
            
            current_x = -left
            current_y = -down
            
            lawn = GridAStar()
            lawn.parseFromList(rows)
            
            print('Lawn ' + str(i) + ' start at ' + str(current_x) + ' ' + str(current_y))
            
            try:
                lawn.get_cell_coord(current_x, current_y).is_passable()
            except:
                print('Invalid cause start oob or impassable')
                output_list.append('INVALID')
                continue
            
            validity = True
            
            if not lawn.get_cell_coord(current_x, current_y).is_passable():
                output_list.append('INVALID')
                continue
            else:
                lawn.get_cell_coord(current_x, current_y).set_tag(CellTags.IMPASSABLE)
            
            for each in path:
                match each:
                    case 'W':
                        current_y -= 1
                        if current_y < 0:
                            print('-yLawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
                            validity = False
                            break
                    case 'D':
                        current_x += 1
                        if current_x >= size[0]:
                            print('+xLawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
                            validity = False
                            break
                    case 'S':
                        current_y += 1
                        if current_y >= size[1]:
                            print('+yLawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
                            validity = False
                            break
                    case 'A':
                        current_x -= 1
                        if current_x < 0:
                            print('-xLawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
                            validity = False
                            break
                    case _:
                        raise Exception('Something went wrong')
                
                print('at ' + str(current_x) + ',' + str(current_y))
                if not lawn.get_cell_coord(current_x, current_y).is_passable():
                    print('impLawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
                    validity = False
                    break
                else:
                    lawn.get_cell_coord(current_x, current_y).set_tag(CellTags.IMPASSABLE)
            
            if validity != False:
                str_list = lawn.get_all_chars()
                print(str_list)
                for each in str_list:
                    if each != 'X':
                        validity = False
                        break
            
            if validity:
                output_list.append('VALID')
            else:
                output_list.append('INVALID')
            
            # outer_valid = False
            
            # start_x = 0
            # start_y = 0
            
            # while start_y < size[1] and outer_valid == False:
            #     start_x = 0
            #     while start_x < size[0] and outer_valid == False:
                    
            #         lawn.parseFromList(rows)
            #         for each in lawn._grid:
                        
                    
            #         current_x = start_x
            #         current_y = start_y
                    
            #         print('Lawn ' + str(i) + ': start_x = ' + str(start_x) + ' start_y = ' + str(start_y))
            
            #         validity = True
            
            #         for each in path:
            #             match each:
            #                 case 'W':
            #                     current_x -= 1
            #                     if current_x < 0:
            #                         validity = False
            #                         print('Lawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
            #                         break
            #                 case 'D':
            #                     current_y += 1
            #                     if current_y >= size[1]:
            #                         validity = False
            #                         print('Lawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
            #                         break
            #                 case 'S':
            #                     current_x += 1
            #                     if current_x >= size[0]:
            #                         validity = False
            #                         print('Lawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
            #                         break
            #                 case 'A':
            #                     current_y -= 1
            #                     if current_y < 0:
            #                         validity = False
            #                         print('Lawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
            #                         break
            #                 case _:
            #                     raise Exception('Something went wrong')

            #             if current_x < 0 or current_x >= size[0] or current_y < size[1] or current_y >= size[1]:
            #                 validity = False
            #                 print('Lawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
            #                 break
            #             if not lawn.get_cell_coord(current_x, current_y).is_passable():
            #                 validity = False
            #                 print('Lawn: ' + str(i) + ' Invalid at ' + str(current_x) + ',' + str(current_y))
            #                 break
            #             else:
            #                 lawn.get_cell_coord(current_x, current_y).set_tag(CellTags.IMPASSABLE)
            
            #         if validity:
            #             output_list.append('VALID')
            #             outer_valid = True
            #             break
                
            #         start_x += 1
            #     start_y += 1
            # output_list.append('INVALID')

        self.file_access.save_file(file, output_list)
        return None