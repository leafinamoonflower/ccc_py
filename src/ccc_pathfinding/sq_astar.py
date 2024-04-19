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
                if c == '.':
                    row_x.append(GridCell(CellTags.PASSABLE))
                elif c == 'X':
                    row_x.append(GridCell(CellTags.IMPASSABLE))
                else:
                    row_x.append(GridCell(CellTags.PASSABLE))
            self._grid.append(row_x)
    
    def get_cell_coord(self, x: int, y: int):
        return self._grid[y][x]
    
    def get_grid(self):
        rows = list()
        for each in self._grid:
            rows.append(each)
        return rows

    def get_all_chars(self):
        chars = str()
        for each in self._grid: #each row
            for c in each:
                if c.is_passable():
                    chars += '.'
                else:
                    chars += 'X'
        return chars