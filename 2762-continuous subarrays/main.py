class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(int)

        # process
        # helper function
        def isValid(num):
            count = 0
            for x in range(-2, 3):
                count += dicts[num + x]
            return count == sum(dicts.values())

        # sliding window
        left, right = 0, 0
        ans = 0
        while right < L:
            dicts[nums[right]] += 1
            while not isValid(nums[right]):
                dicts[nums[left]] -= 1
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
