class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L = len(nums)
        left = 0
        right = 0

        from collections import defaultdict
        dicts = defaultdict(int)
        ans = 0
        while right < L:
            dicts[nums[right]] += 1
            while dicts[nums[right]] > k:
                dicts[nums[left]] -= 1
                left += 1
            right += 1
            ans = max(ans, right - left)
        return ans


nums = [1,2,3,1,2,3,1,2]
k = 2

nums = [1,2,1,2,1,2,1,2]
k = 1

nums = [5,5,5,5,5,5,5]
k = 4

nums = [1,1,1,2,1,2,2,1,2]
k = 2

nums = [1,1,1,3]
k = 2

solution = Solution()
print(solution.maxSubarrayLength(nums, k))


