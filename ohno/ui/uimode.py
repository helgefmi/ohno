class UIMode:
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
