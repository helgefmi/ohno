from ohno.dungeon.feature.basefeature import BaseFeature
from ohno.dungeon.feature.door import Door
from ohno.dungeon.feature.staircase import Staircase

def create(ohno, maptile):
    """Checks `maptile` for which feature to create"""
    if maptile['glyph'] in '-|]' and maptile['color']['fg'] == 33:
        return Door(ohno, maptile)
    elif maptile['glyph'] in '<>':
        return Staircase(ohno, maptile)

    return BaseFeature(ohno, maptile)
