class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        N = len(costs)
        lower = candidates - 1
        upper = N - candidates

        # init
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        if lower < upper:
            for x in range(lower + 1):
                heappush(heap, (costs[x], x))
            for x in range(N - 1, upper - 1, -1):
                heappush(heap, (costs[x], x))
        else:
            for idx, cost in enumerate(costs):
                heappush(heap, (cost, idx))

        # run
        ans = 0
        for x in range(k):
            cost, idx = heappop(heap)
            ans += cost
            if lower < upper - 1:
                if idx <= lower:
                    lower += 1
                    heappush(heap, (costs[lower], lower))
                elif idx >= upper:
                    upper -= 1
                    heappush(heap, (costs[upper], upper))
        return ans


costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4

"""
costs = [1,2,4,1]
k = 3
candidates = 3

costs = [1]
k = 1
candidates = 1

costs = [10,15,23,8,1,2,1,2,1,1,67,8,19,25]
k = 12
candidates = 4

costs = [28,35,21,13,21,72,35,52,74,92,25,65,77,1,73,32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99,83,5,21,76,34]
k = 32
candidates = 12

costs = [18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75]
k = 13
candidates = 23
"""

solution = Solution()
print(solution.totalCost(costs, k, candidates))
