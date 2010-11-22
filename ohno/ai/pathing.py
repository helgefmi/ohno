import heapq
from operator import itemgetter

class Pathing(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self.previous = self.tick = None

    def is_uptodate(self):
        # Have we called search() in this particular tick?
        # Mostly used as a sanity check.
        return self.tick == self.ohno.tick

    def search_where(self, **kwargs):
        def predicate(tile):
            for key, value in kwargs.iteritems():
                attr = getattr(tile, key)
                if callable(attr):
                    attr = attr()
                if value != attr:
                    return False
            return True
        return self._search(predicate)

    def _search(self, predicate):
        assert self.is_uptodate()
        for tile in self.tiles:
            if predicate(tile):
                yield tile

    def search(self):
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

        self.tiles = []
        while graph:
            cur_dist, current = heapq.heappop(graph)

            # Stop when we reach an unreachable tile
            if cur_dist == inf:
                break

            self.tiles.append(current)

            # We can search for an unwalkable tile, but then we can't walk further.
            if not current.walkable:
                continue

            for neighbor in current.adjacent:
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

        assert self.tiles[0] == source

    def get_path(self, tile):
        # Returns an iterator for the path to a particular tile in order.
        assert self.is_uptodate()
        path = []
        while tile != self.ohno.dungeon.curtile:
            path.append(tile)
            tile = self.previous[tile.idx]
        return reversed(path)
