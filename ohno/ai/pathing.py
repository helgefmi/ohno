import heapq

class Pathing(object):
    def __init__(self, ohno):
        self.ohno = ohno

    def search_where(self, **kwargs):
        def predicate(tile):
            for key, value in kwargs.iteritems():
                attr = getattr(tile, key)
                if callable(attr):
                    attr = attr()
                if value != attr:
                    return False
            return True
        return self.search(predicate)

    def search(self, predicate):
        inf = float('inf')

        source = self.ohno.dungeon.curtile
        self.dist = [inf] * 21 * 80
        self.prev = [None] * 21 * 80

        self.dist[source.idx] = 0
        self.graph = [(0, source)]

        while self.graph:
            cur_dist, current = heapq.heappop(self.graph)
            if current != source and predicate(current):
                yield current

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
                # Don't search past two unexplored tiles in a row
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
                self.dist[neighbor.idx] = cur_dist + weight
                self.prev[neighbor.idx] = current
                heapq.heappush(self.graph, (self.dist[neighbor.idx], neighbor))

    def get_path(self, tile):
        path = []
        while tile != self.ohno.dungeon.curtile:
            path.append(tile)
            tile = self.prev[tile.idx]
        return reversed(path)
