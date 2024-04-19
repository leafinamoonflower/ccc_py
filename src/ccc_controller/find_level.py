from ccc_levels.abstract_level import AbstractLevel
from ccc_levels.level1 import Level1
from ccc_levels.level2 import Level2
from ccc_levels.level3 import Level3

def find_level(level_num: int) -> AbstractLevel:
    match level_num:
        case 1:
            return Level1()
        case 2:
            return Level2()
        case 3:
            return Level3()
        case _:
            raise RuntimeError('Input for <LEVEL> was not recognized. Does the Level exist?')