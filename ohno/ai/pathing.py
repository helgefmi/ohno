import heapq

class Pathing:
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
            if dist[current.idx] == inf:
                break
            for neighbor in current.adjacent:
                if not neighbor.walkable:
                    continue
                if prev[neighbor.idx]:
                    continue
                if not current.explored and not neighbor.explored:
                    continue
                can_diagonal = current.can_walk_diagonally() and \
                               neighbor.can_walk_diagonally()
                if not can_diagonal and abs(neighbor.idx - current.idx) not in (1, 80):
                    continue
                alt = dist[current.idx] + 1
                if alt < dist[neighbor.idx]:
                    dist[neighbor.idx] = alt
                    prev[neighbor.idx] = current
                heapq.heappush(graph, (dist[neighbor.idx], neighbor))
        return dist, prev
