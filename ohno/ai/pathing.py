import heapq

class Pathing(object):
    def __init__(self, ohno):
        self.ohno = ohno

    def search(self):
        inf = float('inf')

        source = self.ohno.dungeon.curtile
        dist = [inf] * 21 * 80
        prev = [None] * 21 * 80

        dist[source.idx] = 0
        graph = [(0, source)]

        while graph:
            cur_dist, current = heapq.heappop(graph)
            # Stop when we reach an unreachable tile
            if cur_dist == inf:
                break
            for neighbor in current.adjacent:
                # Investigate each tile once
                if prev[neighbor.idx]:
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
                dist[neighbor.idx] = cur_dist + 1
                prev[neighbor.idx] = current
                heapq.heappush(graph, (dist[neighbor.idx], neighbor))
        return dist, prev
