from levels.abstract_level import AbstractLevel
from levels.level1 import Level1

def find_level(level_num: int) -> AbstractLevel:
    match level_num:
        case 1:
            return Level1()
        case _:
            raise RuntimeError('Input for <LEVEL> was not recognized. Does the Level exist?')