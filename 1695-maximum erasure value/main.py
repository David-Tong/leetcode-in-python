class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(int)

        left = 0
        right = 0
        ans = 0
        score = 0
        while right < L:
            dicts[nums[right]] += 1
            score += nums[right]

            while left < right and dicts[nums[right]] > 1:
                dicts[nums[left]] -= 1
                score -= nums[left]
                left += 1

            ans = max(ans, score)
            right += 1
        return ans


nums = [4,2,4,5,6]
nums = [5,2,1,2,5,2,1,2,5]

solution = Solution()
print(solution.maximumUniqueSubarray(nums))
