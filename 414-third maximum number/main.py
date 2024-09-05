class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for num in nums:
            if num not in heap:
                if len(heap) < 3:
                    heappush(heap, num)
                else:
                    heappush(heap, num)
                    heappop(heap)

        if len(heap) < 3:
            while len(heap) > 1:
                heappop(heap)
        return heappop(heap)


nums = [3,2,1]
nums = [1,2]
nums = [2,2,3,1]
nums = [3,2,1,1,1,1,1]
nums = [5,2,4,1,3,6,0]

solution = Solution()
print(solution.thirdMax(nums))
