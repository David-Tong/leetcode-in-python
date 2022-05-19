class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        N = n + 1
        colors = [0] * N

        from collections import defaultdict
        adjacents = defaultdict(list)
        for dislike in dislikes:
            adjacents[dislike[0]].append(dislike[1])
            adjacents[dislike[1]].append(dislike[0])

        from collections import deque
        bfs = deque()

        for x in range(1, N):
            if colors[x] == 0:
                bfs.append((x, 1))
                while bfs:
                    curr, color = bfs.popleft()
                    for next in adjacents[curr]:
                        if colors[next] == color:
                            return False
                        if colors[next] == 0:
                            colors[next] = -1 * color
                            bfs.append((next, -1 * color))
        return True


n = 4
dislikes = [[1,2],[1,3],[2,4]]

n = 3
dislikes = [[1,2],[1,3],[2,3]]

n = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]

n = 6
dislikes = []

n = 1
dislikes = []

solution = Solution()
print(solution.possibleBipartition(n, dislikes))
