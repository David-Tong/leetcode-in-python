class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        from collections import defaultdict
        vertices = defaultdict(list)
        for idx, employer in enumerate(manager):
            vertices[employer].append(idx)

        from collections import deque
        bfs = deque()
        bfs.append((headID, informTime[headID]))
        ans = 0
        while bfs:
            size = len(bfs)
            for x in range(size):
                curr, time = bfs.popleft()
                ans = max(ans, time)
                for vertex in vertices[curr]:
                    bfs.append((vertex, time + informTime[vertex]))
        return ans

n = 1
headID = 0
manager = [-1]
informTime = [0]

n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]

n = 8
headID = 2
manager = [2,2,-1,2,2,2,1,6]
informTime = [0,2,1,0,0,0,8,0]

"""
n = 8
headID = 0
manager = [-1,5,0,6,7,0,0,0]
informTime = [89,0,0,0,0,523,241,519]
"""

solution = Solution()
print(solution.numOfMinutes(n, headID, manager, informTime))
