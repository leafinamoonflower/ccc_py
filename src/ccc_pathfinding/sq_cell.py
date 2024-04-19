from ccc_pathfinding.cell_tags import CellTags
import math

class GridCell:
    
    # ----- constructor: -----
    
    def __init__(self):
        self._tags = CellTags.PASSABLE
        
        self._parentX = 0
        self._parentY = 0
        
        self._f = math.inf
        self._g = math.inf
        self._h = 0
    
    
    def __init__(self, tag: CellTags):
        self._tags = tag
        
        self._parentX = 0
        self._parentY = 0
        
        self._f = math.inf
        self._g = math.inf
        self._h = 0
    
    # ----- setter and getter: -----
    
    # @_tags.setter
    # def tags(self, tag):
    #     self._tags = tag
        
    
    @property
    def tags(self):
        return self._tags
    
    # ----- methods: -----
    
    def __str__(self) -> str:
        if self._tags == CellTags.PASSABLE:
            return 'P'
        elif self._tags == CellTags.IMPASSABLE:
            return 'I'
        else:
            return '?'
        
    def set_tag(self, tag: CellTags):
        self._tags = tag
    # def addTag(self, tag: CellTags):
    #     if self._tags.count(tag) > 0:
    #         return
    #     if tag == CellTags.PASSABLE and self._tags.count(CellTags.IMPASSABLE) > 0:
    #         self.deleteTag(CellTags.IMPASSABLE)
    #     elif tag == CellTags.IMPASSABLE and self._tags.count(CellTags.PASSABLE) > 0:
    #         self.deleteTag(CellTags.PASSABLE)
    #     temp: list = self._tags
    #     temp.append(tag)
    #     self._tags = temp
    
    
    # def deleteTag(self, tag: CellTags):
    #     while self._tags.count(tag) > 0:
    #         temp: list = self._tags
    #         temp.remove(tag)
    #     self._tags = temp
    
    def is_passable(self) -> bool:
        if self.tags == CellTags.PASSABLE:
            return True
        return False