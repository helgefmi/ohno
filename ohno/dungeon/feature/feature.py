from ohno.dungeon.feature.basefeature import BaseFeature
from ohno.dungeon.feature.door import Door

def create(ohno, maptile):
    """Checks `maptile` for which feature to create"""
    if maptile['glyph'] in '-|]' and maptile['color']['fg'] == 33:
        return Door(ohno, maptile)

    return BaseFeature(ohno, maptile)
