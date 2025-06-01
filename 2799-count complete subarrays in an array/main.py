class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        distinct = set()
        for num in nums:
            distinct.add(num)
        D = len(distinct)

        # process
        from collections import defaultdict
        dicts = defaultdict(int)
        left, right = 0, 0
        ans = 0
        while left < L:
            while right < L and len(dicts) < D:
                dicts[nums[right]] += 1
                right += 1

            if len(dicts) == D:
               ans += L - right + 1

            dicts[nums[left]] -= 1
            if dicts[nums[left]] == 0:
                del dicts[nums[left]]
            left += 1

        return ans


nums = [1,3,1,2,2]
nums = [5,5,5,5]
nums = [1]
nums = [1,2,1,2,1,2]

solution = Solution()
print(solution.countCompleteSubarrays(nums))
