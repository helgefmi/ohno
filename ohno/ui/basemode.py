class BaseMode(object):
    """
    Meant as an abstract class with sane defaults for creating new UI modes.
    """
    def tile_to_glyph(self, tile):
        """Takes a tile and outputs a character."""
        return ord(tile.appearance.glyph)

    def tile_to_color(self, tile):
        """Takes a tile and outputs a curses color code."""
        return self.ohno.ui.curses.convert_color(tile.appearance)

    def first_botline(self):
        hero = self.ohno.hero
        return 'P:%2d,%2d' % (hero.position.x, hero.position.y)

    def second_botline(self):
        hero = self.ohno.hero
        return 'D:%d H:%d/%d A:%d X:%d T:%d $%d' % (
            hero.dlvl, hero.hp, hero.maxhp, hero.ac, hero.level,
            hero.turns, hero.gold
        )
    
    def on_input(self, input):
        if input == '|':
            self.ohno.ui.open_console()
        elif input == 's':
            self.ohno.save()
        elif input == 'p':
            self.ohno.paused = not self.ohno.paused
