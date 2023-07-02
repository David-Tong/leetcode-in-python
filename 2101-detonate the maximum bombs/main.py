class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        def canUnion(bomb, bomb2):
            distance = (bomb[0] - bomb2[0]) ** 2 + (bomb[1] - bomb2[1]) ** 2
            radius = bomb[2] ** 2
            if distance <= radius:
                return True
            else:
                return False

        # pre-process
        N = len(bombs)
        connections = [[False] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if canUnion(bombs[x], bombs[y]):
                    connections[x][y] = True

        def findMax(idx):
            from collections import deque
            bfs = deque()
            visited = [False] * N
            bfs.append(idx)
            visited[idx] = True

            ans = 1
            while bfs:
                curr = bfs.popleft()
                for x in range(N):
                    if not visited[x] and connections[curr][x]:
                        ans += 1
                        bfs.append(x)
                        visited[x] = True
            return ans

        ans = 0
        for x in range(N):
            ans = max(ans, findMax(x))
        return ans


bombs = [[2,1,3],[6,1,4]]
bombs = [[1,1,5],[10,10,5]]
bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
bombs = [[1,1,1]]
bombs = [[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]

solution = Solution()
print(solution.maximumDetonation(bombs))
