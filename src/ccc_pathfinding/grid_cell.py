from ccc_pathfinding.cell_tags import CellTags
import math

class GridCell:
    
    # ----- constructor: -----
    
    def __init__(self):
        self._tags = list()
        
        self._parentX = 0
        self._parentY = 0
        
        self._f = math.inf
        self._g = math.inf
        self._h = 0
    
    # ----- methods: -----
        
    def addTag(self, tag: CellTags):
        temp: list = self._tags
        temp.append(tag)
        self._tags = temp
        