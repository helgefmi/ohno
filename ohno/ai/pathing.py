import heapq
from operator import itemgetter

class Pathing(object):
    def __init__(self, ohno):
        self.ohno = ohno
        self.tick = None

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
        distances = [inf] * 21 * 80
        self.prev = [None] * 21 * 80

        distances[source.idx] = 0
        graph = [(0, source)]

        while graph:
            cur_dist, current = heapq.heappop(graph)

            # Stop when we reach an unreachable tile
            if cur_dist == inf:
                break
            for neighbor in current.adjacent:
                # Investigate each tile once
                if self.prev[neighbor.idx]:
                    continue
                # Can't walk through walls
                if not neighbor.walkable:
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
                    weight -= 0.95
                distances[neighbor.idx] = cur_dist + weight
                self.prev[neighbor.idx] = current
                heapq.heappush(graph, (distances[neighbor.idx], neighbor))

        sorted_indices = sorted(enumerate(distances), key=itemgetter(1))
        self.tiles = [self.ohno.dungeon.curlevel.tiles[idx] for idx, dist in sorted_indices if dist != inf]

    def get_path(self, tile):
        assert self.is_uptodate()
        path = []
        while tile != self.ohno.dungeon.curtile:
            path.append(tile)
            tile = self.prev[tile.idx]
        return reversed(path)
