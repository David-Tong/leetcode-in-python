class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(online)

        # collect all edge costs for binary search
        costs = sorted(set(c for _, _, c in edges))
        if not costs:
            return -1

        # build graph
        from collections import defaultdict
        graph = defaultdict(list)
        indegree_full = [0] * L

        for u, v, c in edges:
            graph[u].append((v, c))
            indegree_full[v] += 1

        # topological sort (once)
        from collections import deque
        def topology_sort():
            indegree = indegree_full[:]  # copy
            q = deque(i for i in range(L) if indegree[i] == 0)
            order = []
            while q:
                u = q.popleft()
                order.append(u)
                for v, _ in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
            return order

        topology = topology_sort()
        if len(topology) < L:
            return -1  # graph must be DAG

        # process
        # dp method
        # check feasibility for bottleneck target
        def can_achieve(target):
            dp_cost = [float("inf")] * L
            dp_cost[0] = 0

            for u in topology:
                if not online[u]:
                    continue
                if dp_cost[u] == float("inf"):
                    continue

                for v, c in graph[u]:
                    if not online[v]:
                        continue
                    if c < target:
                        continue  # edge doesn't meet bottleneck threshold

                    new_cost = dp_cost[u] + c
                    if new_cost < dp_cost[v]:
                        dp_cost[v] = new_cost

            return dp_cost[L - 1] <= k

        # binary search
        left, right = 0, len(costs) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if can_achieve(costs[middle]):
                left = middle
            else:
                right = middle - 1
        if can_achieve(costs[right]):
            idx = right
        elif can_achieve(costs[left]):
            idx = left
        else:
            idx = -1

        # post-process
        ans = -1
        if idx >= 0:
            ans = costs[idx]
        return ans


edges = [[0,1,5], [1,3,10], [0,2,3], [2,3,4]]
online = [True, True, True, True]
k = 10

edges = [[0,1,7], [1,4,5], [0,2,6], [2,3,6], [3,4,2], [2,4,6]]
online = [True, True, True, False, True]
k = 12

solution = Solution()
print(solution.findMaxPathScore(edges, online, k))
