class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(list)
        for flight in flights:
            dicts[flight[0]].append((flight[1], flight[2]))

        from collections import deque
        bfs = deque()
        visited = [float("inf")] * n
        bfs.append((src, 0))
        visited[src] = 0

        stops = 0
        ans = float("inf")
        while bfs:
            size = len(bfs)
            for x in range(size):
                curr, cost = bfs.popleft()
                for node, price in dicts[curr]:
                    if cost + price < visited[node]:
                        bfs.append((node, cost + price))
                        visited[node] = cost + price
                        if node == dst:
                            ans = min(ans, cost + price)
            stops += 1
            if stops > k:
                break

        return -1 if ans == float("inf") else ans


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0

n = 2
flights = []
src = 0
dst = 1
k = 1

solution = Solution()
print(solution.findCheapestPrice(n, flights, src, dst, k))
