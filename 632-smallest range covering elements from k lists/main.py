class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        left = float("inf")
        right = float("-inf")
        range = float("inf")


        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        for seq, num in enumerate(nums):
            right = max(right, nums[seq][0])
            heappush(heap, (nums[seq][0], seq, 0))

        ans = [left, right]
        while heap:
            left, seq, idx = heappop(heap)
            if right - left < range:
                ans[0] = left
                ans[1] = right
                range = right - left

            # stop condition
            if idx == len(nums[seq]) - 1:
                break
            right = max(right, nums[seq][idx + 1])
            heappush(heap, (nums[seq][idx + 1], seq, idx + 1))

        return ans


nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
nums = [[1,2,3],[1,2,3],[1,2,3]]

solution = Solution()
print(solution.smallestRange(nums))
