import bpython

class NormalMode:
    def __init__(self, ohno):
        self.ohno = ohno
        self.ohno.paused = False

    def on_input(self, input):
        if input == '|':
            # Opens up a bpython REPL.
            embedded_locals = {
                'ohno': self.ohno
            }
            bpython.embed(locals_=embedded_locals)
            self.ohno.ui.curses.init_colors()
        elif input == 's':
            self.ohno.save()
        elif input == 'p':
            self.ohno.paused = not self.ohno.paused
        elif input == 'd':
            from ohno.ui.debugmode import DebugMode
            self.ohno.ui.set_mode(DebugMode(self.ohno))

    def tile_to_glyph(self, tile):
        return ord(tile.glyph)

    def tile_to_color(self, tile):
        return self.ohno.ui.curses.convert_color(tile.color)

    def first_botline(self):
        hero = self.ohno.hero
        return 'P:%2d,%2d' % (hero.position[0], hero.position[1])

    def secound_botline(self):
        hero = self.ohno.hero
        return 'D:%d H:%d/%d A:%d X:%d T:%d $%d' % (hero.dlvl, hero.hp, hero.maxhp, hero.ac, hero.level, hero.turns, hero.gold)
