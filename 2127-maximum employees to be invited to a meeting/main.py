class Solution(object):
    def maximumInvitations(self, favorite):
        """
        :type favorite: List[int]
        :rtype: int
        """
        # pre-process
        N = len(favorite)
        ingrees = [0] * N
        for fvr in favorite:
            ingrees[fvr] += 1

        # topological sort
        from collections import deque
        bfs = deque()
        visited = [False] * N
        depths = [1] * N

        for x in range(N):
            if ingrees[x] == 0:
                bfs.append(x)
                visited[x] = True

        while bfs:
            curr = bfs.popleft()
            nxt = favorite[curr]
            ingrees[nxt] -= 1
            if ingrees[nxt] == 0:
                if not visited[nxt]:
                    bfs.append(nxt)
                    visited[nxt] = True
            depths[nxt] = depths[curr] + 1

        # process
        # case 1 : max multiple node circle
        # case 2 : the sum links to 2 nodes circle
        max_multi_node_circle = 0
        sum_links = 0
        for x in range(N):
            if not visited[x]:
                count = 0
                y = x
                while not visited[y]:
                    count += 1
                    visited[y] = True
                    y = favorite[y]

                # case 1
                if count >= 3:
                    max_multi_node_circle = max(max_multi_node_circle, count)
                # case 2
                if count == 2:
                    start, end = x, favorite[x]
                    sum_links += depths[start] + depths[end]
        return max(max_multi_node_circle, sum_links)


favorite = [2,2,1,2]
favorite = [1,2,0]
favorite = [3,0,1,4,1]

solution = Solution()
print(solution.maximumInvitations(favorite))
