class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        visited = [0] * N

        from collections import deque
        bfs = deque()
        bfs.append(0)
        visited[0] = 1
        while bfs:
            room = bfs.popleft()
            for key in rooms[room]:
                if visited[key] == 0:
                    bfs.append(key)
                    visited[key] = 1

        if sum(visited) == N:
            return True
        else:
            return False


rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]
rooms = [[], [1]]

solution = Solution()
print(solution.canVisitAllRooms(rooms))
