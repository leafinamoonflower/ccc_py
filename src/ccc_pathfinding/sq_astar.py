from ccc_pathfinding.cell_tags import CellTags
from ccc_pathfinding.sq_cell import GridCell

class GridAStar:
    
    # ----- constructor: -----
    
    def __init__(self):
        self._grid: list = None
    
    # ----- methods: -----
    
    def parseFromList(self, lists: list):
        self._grid = list()
        for l in lists:
            row_x = list()
            for c in l:
                if c == 'O':
                    row_x.append(GridCell(CellTags.PASSABLE))
                elif c == 'X':
                    row_x.append(GridCell(CellTags.IMPASSABLE))
                else:
                    print('couldn\'t parse cell (O/X), creating empty')
                    row_x.append(GridCell(CellTags.PASSABLE))
            self._grid.append(row_x)
                
            
        # printing         
        for r in self._grid:
            for e in r:
                print(e, end='')
            print('')
    
    