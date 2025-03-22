class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from heapq import heapify, heappush, heappop
        mini, maxi = list(), list()
        heapify(mini), heapify(maxi)

        # process
        # helper function
        def isValid(left, right):
            while mini and mini[0][1] < left:
                heappop(mini)
            while maxi and maxi[0][1] < left:
                heappop(maxi)

            if mini and abs(mini[0][0] - nums[right]) > 2:
                return False
            if maxi and abs(-1 * maxi[0][0] - nums[right]) > 2:
                return False
            return True

        # sliding window
        left, right = 0, 0
        ans = 0
        while right < L:
            heappush(mini, (nums[right], right))
            heappush(maxi, (-1 * nums[right], right))
            while not isValid(left, right):
                left += 1
            right += 1
            ans += right - left
        return ans


nums = [5,4,2,4]
nums = [1,2,3]
nums = [1]
nums = [1,1,1,1,2,1,2,23,32,22,1]

solution = Solution()
print(solution.continuousSubarrays(nums))