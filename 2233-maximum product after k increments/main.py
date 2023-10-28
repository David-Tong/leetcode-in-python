class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for num in nums:
            heappush(heap, num)

        for x in range(k):
            item = heappop(heap) + 1
            heappush(heap, item)

        ans = 1
        while heap:
            ans = (ans * heappop(heap)) % MODULO
        return ans % MODULO


nums = [0,4]
k = 5

nums = [6,3,3,2]
k = 2

nums = [0]
k = 1

solution = Solution()
print(solution.maximumProduct(nums, k))
