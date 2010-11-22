from ohno.dungeon.feature.staircase import Staircase
from ohno.ai.strategy.basestrategy import BaseStrategy

from ohno.action.open import Open
from ohno.action.kick import Kick
from ohno.action.walk import Walk
from ohno.action.usestairs import UseStairs
from ohno.action.search import Search

# TODO: get_action should return a closed door or unexplored walkable tile
#       according to which is the closest instead of doing one first, then the
#       other.
class Explore(BaseStrategy):
    def _unexplored(self):
        tile = self.ohno.ai.pathing.search_where(explored=False, walkable=True).next()
        self.ohno.logger.strategy('[explore] found unexplored at %r' % tile)
        return Walk(self.ohno, tile=tile)

    def _closed_doors(self):
        tile = self.ohno.ai.pathing.search_where(has_closed_door=True).next()
        assert tile.walkable == False

        if self.explored_progress >= 100:
            self.ohno.logger.strategy('[explore] I\'ve explored enough, won\'t open door')
            return

        self.ohno.logger.strategy('[explore] found closed door at %r' % tile)
        if tile in self.ohno.dungeon.curtile.adjacent:
            if tile.feature.locked:
                self.ohno.logger.strategy('[explore] door is locked; kicking..')
                return Kick(self.ohno, tile=tile)
            else:
                self.ohno.logger.strategy('[explore] door is not locked; opening..')
                return Open(self.ohno, tile=tile)
        else:
            self.ohno.logger.strategy('[explore] door is not adjacent; walking..')
            return Walk(self.ohno, tile=tile)

    def _descend(self):
        curtile = self.ohno.dungeon.curtile
        if curtile.feature_is_a('Staircase') and\
           curtile.feature.direction == 'down':
           return UseStairs(self.ohno, tile=curtile)
        else:
            for tile in self.ohno.ai.pathing.search_where(feature_name='Staircase'):
                if tile.feature.direction == 'down':
                    return Walk(self.ohno, tile=tile)
    
    def _search(self):
        # TODO: Need to have a fallback too..
        # TODO: Use pathing instead, and check if you have a path to '>' aswell.
        if self.explored_progress > 80.0:
            self.ohno.logger.strategy('[explore] I\'ve explored enough, won\'t search')
            return

        # 1. Find walls
        self.ohno.logger.strategy('[explore] finding walls..')
        walls = self.ohno.ai.pathing.search_where(is_wall=True)
        good_targets = []
        sort_dict = {}
        bad_max_search = False
        self.ohno.logger.strategy('[explore] iterating walls..')
        for wall in walls:
            # 2. If we have searched this tile enough, skip it. We will search
            #    it again when everything is searched "enough".
            if wall.searched >= self.ohno.dungeon.curlevel.max_searched:
                bad_max_search = True
                continue

            # 3. Filter out walls that have more than one orthogonal walkable, reachable tile
            reachable = [o for o in wall.orthogonal if o.walkable and o.reachable]
            if len(reachable) != 1:
                continue

            # 4. Check if another wall benefits from searching this wall aswell.
            #    The more orthogonal reachable tiles, the better.
            target = reachable[0]
            sort_dict[target.idx] = sort_dict.get(target.idx, 0) - 1

            # 5. Check if we're in the middle of a hallway:
            #   ##-
            # #@# |
            # #   |
            if sum(1 for o in target.horizontal if o.is_hallway) == 2 or\
               sum(1 for o in target.vertical if o.is_hallway) == 2:
               continue

            good_targets.append(target)

        # If we didn't find anything but skipped a wall because of max_searched,
        # we'll up max_searched and recurse.
        if bad_max_search and not good_targets:
            self.ohno.logger.strategy('[explore] recursing due to bad_max_search..')
            self.ohno.dungeon.curlevel.max_searched += 10
            return self._search()

        self.ohno.logger.strategy('[explore] found some good targets: %s' % good_targets)

        tile = sorted(
            good_targets,
            key=lambda t:(sort_dict[t.idx], t.distance_from_hero())
        )[0]
        self.ohno.logger.strategy('[explore] found a tile to search: %r' % tile)
        if tile == self.ohno.dungeon.curtile:
            self.ohno.logger.strategy('[explore] we\'re adjacent; searching..')
            return Search(self.ohno)
        else:
            self.ohno.logger.strategy('[explore] we\'re not close enough; walking there..')
            return Walk(self.ohno, tile=tile)

    def get_action(self):
        self.explored_progress = self.ohno.dungeon.curlevel.explored_progress()
        self.ohno.logger.strategy('[explore] explored_progress is %f' % self.explored_progress)
        for method in (self._unexplored, self._closed_doors,
                       self._search, self._descend):
            try:
                result = method()
                if result:
                    return result
            except StopIteration:
                self.ohno.logger.strategy('[explore] StopIteration at %r' % method)
