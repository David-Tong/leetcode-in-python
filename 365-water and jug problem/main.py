class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        def canMeasure(jug1, jug2, targetCapacity):
            if jug1 == targetCapacity:
                return True
            if jug2 == targetCapacity:
                return True
            if jug1 + jug2 == targetCapacity:
                return True
            return False

        from collections import deque
        bfs = deque()
        visited = set()
        # start from different possible status
        origins = [(0, 0), (jug1Capacity, 0), (0, jug2Capacity), (jug1Capacity, jug2Capacity)]
        for origin in origins:
            jug1, jug2 = origin
            if canMeasure(jug1, jug2, targetCapacity):
                return True
            bfs.append(origin)
            visited.add(origin)
        while bfs:
            jug1, jug2 = bfs.popleft()
            nexts = list()
            nexts.append((jug1, 0))
            nexts.append((0, jug2))
            nexts.append((jug1, jug2Capacity))
            nexts.append((jug1Capacity, jug2))
            if jug1 + jug2 >= jug1Capacity:
                nexts.append((jug1Capacity, jug2 - (jug1Capacity - jug1)))
            elif jug1 + jug2 < jug1Capacity:
                nexts.append((jug1 + jug2, 0))
            if jug1 + jug2 >= jug2Capacity:
                nexts.append((jug1 - (jug2Capacity - jug2), jug2Capacity))
            elif jug1 + jug2 < jug2Capacity:
                nexts.append((0, jug1 + jug2))
            for next in nexts:
                if next not in visited:
                    next_jug1, next_jug2 = next
                    if canMeasure(next_jug1, next_jug2, targetCapacity):
                        return True
                    bfs.append(next)
                    visited.add(next)
        return False


jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4

jug1Capacity = 2
jug2Capacity = 6
targetCapacity = 5

jug1Capacity = 1
jug2Capacity = 2
targetCapacity = 3

solution = Solution()
print(solution.canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))
