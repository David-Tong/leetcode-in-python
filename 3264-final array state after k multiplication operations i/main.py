class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        # pre-process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for idx, num in enumerate(nums):
            heappush(heap, (num, idx))

        # process
        for _ in range(k):
            item, idx = heappop(heap)
            nums[idx] = item * multiplier
            heappush(heap, (item * multiplier, idx))
        return nums


nums = [2,1,3,5,6]
k = 5
multiplier = 2

nums = [1,2]
k = 3
multiplier = 4

solution = Solution()
print(solution.getFinalState(nums, k, multiplier))
