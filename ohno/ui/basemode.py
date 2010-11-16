import bpython

class BaseMode(object):
    """
    Meant as an abstract class with sane defaults for creating new UI modes.
    """
    def tile_to_glyph(self, tile):
        """Takes a tile and outputs a character."""
        return ord(tile.appearance['glyph'])

    def tile_to_color(self, tile):
        """Takes a tile and outputs a curses color code."""
        return self.ohno.ui.curses.convert_color(tile.appearance['color'])

    def first_botline(self):
        hero = self.ohno.hero
        return 'P:%2d,%2d' % (hero.position[0], hero.position[1])

    def secound_botline(self):
        hero = self.ohno.hero
        return 'D:%d H:%d/%d A:%d X:%d T:%d $%d' % (\
                    hero.dlvl, hero.hp, hero.maxhp, hero.ac, hero.level,\
                    hero.turns, hero.gold)
    
    def on_input(self, input):
        if input == '|':
            # Opens up a bpython REPL.
            embedded_locals = {
                'ohno': self.ohno
            }
            bpython.embed(locals_=embedded_locals)
            # Since bpython will modify our curses setup, we need to
            # reinitialize curses (nodelay, noecho, ..).
            self.ohno.ui.curses.start_curses()
        elif input == 's':
            self.ohno.save()
        elif input == 'p':
            self.ohno.paused = not self.ohno.paused
