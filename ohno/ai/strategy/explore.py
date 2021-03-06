from ohno.ai.strategy.basestrategy import BaseStrategy

from ohno.action.open import Open
from ohno.action.kick import Kick
from ohno.action.walk import Walk
from ohno.action.usestairs import UseStairs
from ohno.action.search import Search

class Explore(BaseStrategy):
    def _unexplored(self):
        tile = self.ohno.ai.pathing.search(explored=False, walkable=True).next()
        self.ohno.logger.strategy('[explore] found unexplored at %r' % tile)
        return Walk(self.ohno, tile=tile)

    def _closed_doors(self):
        if self.downstairs and self.explored_progress >= 100:
            # TODO: Open door if it's close
            self.ohno.logger.strategy('[explore] I\'ve explored enough, won\'t open door')
            return

        tile = self.ohno.ai.pathing.search(has_closed_door=True).next()
        self.ohno.logger.strategy('[explore] found closed door at %r' % tile)

        assert tile.walkable == False, tile
        assert tile.feature_isa('Door'), tile

        if tile in self.ohno.dungeon.curtile.adjacent():
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
        if curtile in self.downstairs:
           return UseStairs(self.ohno, tile=curtile)
        elif self.downstairs:
            return Walk(self.ohno, tile=self.downstairs[0])
    
    def _search(self):
        if self.downstairs and self.explored_progress > 80.0:
            self.ohno.logger.strategy('[explore] I\'ve explored enough, won\'t search')
            return

        # 1. Find walls.
        self.ohno.logger.strategy('[explore] finding walls..')
        walls = self.ohno.ai.pathing.search(is_wall=True)
        good_targets = []

        bad_max_search = False

        sort_dict = {}
        self.ohno.logger.strategy('[explore] iterating %d walls..')
        for wall in walls:
            # 2. If we have searched this tile enough, skip it. We will search
            #    it again when everything else is searched "enough" too.
            if wall.searched >= self.ohno.dungeon.curlevel.max_searched:
                bad_max_search = True
                continue

            # 3. Filter out walls that have more than one orthogonal walkable,
            #    reachable tile.
            reachable = list(wall.orthogonal(walkable=True, reachable=True))
            if len(reachable) != 1:
                continue

            # 4. Check if other walls benefits from searching this wall aswell.
            #    The more orthogonal reachable tiles, the better.
            target = reachable[0]
            sort_dict[target.idx] = sort_dict.get(target.idx, 0) - 1

            # 5. Exclude some scenarios

            # More than one adjacent hallway tile
            #   ##
            # #@#
            # #
            hallways = list(target.orthogonal(is_hallway=True))
            walkables = list(target.orthogonal(walkable=True))
            if len(hallways) > 1:
               continue
            # Between a hallway and floortile
            #   @.
            # ###
            # #
            if hallways and len(walkables) >= 2:
                continue

            # Priority reductions
            # In a corner of a room or hallway
            # |..
            # |@.
            # ---
            if (len(list(target.orthogonal(is_wall=True))) == 2 and
                len(list(target.horizontal(is_wall=True))) == 1):
                sort_dict[target.idx] += 2

            good_targets.append(target)

        # If we didn't find anything but skipped a wall because of `max_searched`,
        # we'll increment `max_searched` and recurse.
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
        # TODO: This is just so I have something to play with. This design is
        #       not nearly as flexible as I want it. I want the different parts
        #       of `explore` to communicate with each other; opening doors on
        #       the way to an unexpored tile, searching if there's a really
        #       good spot close by, etc.
        self.explored_progress = self.ohno.dungeon.curlevel.explored_progress()
        # TODO: queryable should make this prettier
        self.downstairs = [
            tile for tile in self.ohno.ai.pathing.search(feature_name='Staircase')
                    if tile.feature.direction == 'down'
        ]
        self.ohno.logger.strategy('[explore] explored_progress is %f' % self.explored_progress)
        for method in (self._closed_doors, self._descend, self._unexplored,
                       self._search):
            try:
                result = method()
                if result:
                    return result
            except StopIteration:
                self.ohno.logger.strategy('[explore] StopIteration at %r' % method)
