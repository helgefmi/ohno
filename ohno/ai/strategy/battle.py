from ohno.ai.strategy.basestrategy import BaseStrategy
from ohno.action.walk import Walk
from ohno.action.melee import Melee

class Battle(BaseStrategy):
    """Beats up monsters"""
    def get_action(self):
        # TODO: This is obviously too simple.
        #       In the future, `Battle` should be able to melee, throw items,
        #       use magic wands, escape, use scrolls both defensively and
        #       offensively, position itself strategically, and know how to
        #       handle big packs of monsters (who to attack first?)
        monsters = self.ohno.ai.pathing.search(has_monster=True) 
        try:
            tile = monsters.next()
            self.ohno.logger.strategy('[battle] Found monster at: %r' % tile)
            if tile in self.ohno.dungeon.curtile.adjacent():
                self.ohno.logger.strategy('[battle] Monster is adjacent; attacking!')
                return Melee(self.ohno, tile=tile)
            else:
                self.ohno.logger.strategy('[battle] Monster not adjacent; walking there..')
                return Walk(self.ohno, tile=tile)
        except StopIteration:
            pass
