import heapq
from operator import itemgetter

from queryable import queryable

class Pathing(object):
    """
    Handles the pathing for our Hero!
    """
    def __init__(self, ohno):
        self.ohno = ohno
        self.previous = self.tick = None

    def is_uptodate(self):
        """
        Have we called search() in this particular tick?
        Mostly used as a sanity check.
        """
        return self.tick == self.ohno.tick

    @queryable
    def search(self):
        """
        Executes our dijkstra algorithm if we haven't searched yet this turn,
        and returns an iterator which gives us every reachable tile we see,
        starting with the nearest one.
        """
        if not self.is_uptodate():
            self._search()
        return iter(self._tiles)

    def _search(self):
        """
        Dijkstra implementation.
        When executed, the following gets set:
        - self.dists contains the distance_from_hero of every square.
        - self.previous can be used to find the full path from the hero
          to that square.
        - self._tiles will contain all the reachable squares in order of
          smallest distance first.

        Should be executed once every tick (that is, one iteration of Ohno.loop)
        """
        # Make sure we don't call this function more than once each tick, since
        # the pathing obviously can't change untill we do an action.
        assert self.tick != self.ohno.tick
        self.tick = self.ohno.tick

        inf = float('inf')

        source = self.ohno.dungeon.curtile
        assert source.walkable

        self.dists = [inf] * 21 * 80
        self.previous = [None] * 21 * 80

        self.dists[source.idx] = 0
        self.previous[source.idx] = source
        graph = [(0, source)]

        self._tiles = []
        while graph:
            cur_dist, current = heapq.heappop(graph)

            # Stop when we reach an unreachable tile
            if cur_dist == inf:
                break

            self._tiles.append(current)

            # We can search for an unwalkable tile, but then we can't walk further.
            if not current.walkable:
                continue

            for neighbor in current.adjacent():
                # Investigate each tile once
                if self.previous[neighbor.idx]:
                    continue
                # Don't search past two unexplored tiles in a direction
                if not current.explored and not neighbor.explored:
                    continue
                # TODO: Remove can_walk_diagonally and is_open_door and put the
                # logic in here.
                # We can't move diagonally through an open door
                can_diagonal = current.can_walk_diagonally() and \
                               neighbor.can_walk_diagonally()
                if not can_diagonal and abs(neighbor.idx - current.idx) not in (1, 80):
                    continue
                # Set the distance to the neighbor square
                weight = 1
                # Diagonal movement weighs a little bit more than vertical and
                # horizontal movement, because this behaviour explores a little
                # bit better in corridors.
                if abs(neighbor.idx - current.idx) in (1, 80):
                    weight -= 0.01
                self.dists[neighbor.idx] = cur_dist + weight
                self.previous[neighbor.idx] = current
                heapq.heappush(graph, (self.dists[neighbor.idx], neighbor))

        assert self._tiles[0] == source

    def get_path(self, tile):
        # Returns an iterator for the path to a particular tile in order.
        assert self.is_uptodate()
        path = []
        while tile != self.ohno.dungeon.curtile:
            path.append(tile)
            tile = self.previous[tile.idx]
        return reversed(path)
