class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        # sliding window
        right = 0
        pairs = 0
        ans = 0
        for left in range(L):
            while right < L and pairs < k:
                if dicts[nums[right]] > 0:
                    pairs += dicts[nums[right]]
                dicts[nums[right]] += 1
                right += 1

            if pairs >= k:
                ans += L - right + 1
            dicts[nums[left]] -= 1
            if dicts[nums[left]] > 0:
                pairs -= dicts[nums[left]]
        return ans


nums = [1,1,1,1,1]
k = 10

nums = [2,1,1,1,1,1,1]
k = 10

nums = [3,1,4,3,2,2,4]
k = 2

solution = Solution()
print(solution.countGood(nums, k))
