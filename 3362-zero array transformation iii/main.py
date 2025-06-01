class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        Q = len(queries)
        differences = [0] * (L + 1)
        queries = sorted(queries, key=lambda x: x[0])

        # process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        operation = 0
        idx2 = 0
        for idx, num in enumerate(nums):
            operation += differences[idx]
            while idx2 < Q and queries[idx2][0] <= idx:
                heappush(heap, -1 * queries[idx2][1])
                differences[queries[idx2][0]] += 1
                idx2 += 1
            while operation < num and heap and -1 * heap[0] >= idx:
                differences[-1 * heappop(heap) + 1] -= 1
                operation += 1
            if operation < num:
                return -1

        # post-process
        ans = len(heap)
        return ans


nums = [2,0,2]
queries = [[0,2],[0,2],[1,1]]

nums = [2,0,2,2]
queries = [[0,2],[0,2],[1,1]]

nums = [1,1,1,1]
queries = [[1,3],[0,2],[1,3],[1,2]]

nums = [1,2,3,4]
queries = [[0,3]]

solution = Solution()
print(solution.maxRemoval(nums, queries))
