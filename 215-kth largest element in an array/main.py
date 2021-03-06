class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import heapify, heappush, heappop
        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heappop(heap)


nums = [3, 2, 1, 5, 6, 4]
k = 2

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

solution = Solution()
print(solution.findKthLargest(nums, k))
