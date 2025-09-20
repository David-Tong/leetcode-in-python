class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        # pre-process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        # process
        for num in nums:
            heappush(heap, int(num))
            while len(heap) > k:
                heappop(heap)
        ans = str(heappop(heap))
        return ans


nums = ["3","6","7","10"]
k = 4

solution = Solution()
print(solution.kthLargestNumber(nums, k))
