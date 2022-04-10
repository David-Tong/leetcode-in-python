class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            heapq.heappush(stones, stone - stone2)

        return -1 * stones[0]


stones = [2, 7, 4, 1, 8, 1]
stones = [1]
stones = [10, 18, 25, 3, 4, 7, 1]

solution = Solution()
print(solution.lastStoneWeight(stones))
