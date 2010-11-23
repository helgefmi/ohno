from ohno.ai.strategy.basestrategy import BaseStrategy
from ohno.action.walk import Walk
from ohno.action.melee import Melee

class Battle(BaseStrategy):
    def get_action(self):
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
