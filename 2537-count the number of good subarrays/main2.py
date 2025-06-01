class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # helper function
        # pairs - count number of pair
        def pairs(n):
            return n * (n - 1) // 2

        # validate - check if the subarray is validate
        def validate():
            total = 0
            for num in dicts:
                total += pairs(dicts[num])
                if total >= k:
                    return True
            return False

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        # sliding window
        right = 0
        ans = 0
        for left in range(L):
            while right < L and not validate():
                dicts[nums[right]] += 1
                right += 1

            if validate():
                ans += L - right + 1
            dicts[nums[left]] -= 1
        return ans


nums = [1,1,1,1,1]
k = 10

nums = [2,1,1,1,1,1,1]
k = 10

nums = [3,1,4,3,2,2,4]
k = 2

solution = Solution()
print(solution.countGood(nums, k))
