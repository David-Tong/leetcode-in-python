class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        maxi = max(nums)
        indexes = list()
        for idx, num in enumerate(nums):
            if num == maxi:
                indexes.append(idx)
        print(indexes)

        # process
        ans = 0
        for idx, index in enumerate(indexes):
            if idx >= k - 1:
                if idx == len(indexes) - 1:
                    ans += (indexes[idx - k + 1] + 1) * (L - index)
                else:
                    ans += (indexes[idx - k + 1] + 1) * (indexes[idx + 1] - index)
        return ans


nums = [1,3,2,3,3]
k = 2

nums = [1,4,2,1]
k = 3

nums = [1,3,2,2,3,2,2,3,3,3,2,3,2,1]
k = 5

solution = Solution()
print(solution.countSubarrays(nums, k))
