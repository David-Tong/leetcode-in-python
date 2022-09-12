class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def score(prefixes, idx, x, k):
            return False if (prefixes[idx + 1] - prefixes[x]) * (idx - x + 1) >= k else True

        N = len(nums)
        prefixes = list()
        prefixes.append(0)
        for num in nums:
            prefixes.append(prefixes[-1] + num)

        ans = 0
        for idx, num in enumerate(nums):
            left = 0
            right = idx
            while left + 1 < right:
                middle = (left + right) // 2
                if score(prefixes, idx, middle, k):
                    right = middle
                else:
                    left = middle + 1

            if score(prefixes, idx, left, k):
                ans += idx - left + 1
            elif score(prefixes, idx, right, k):
                ans += idx - right + 1
            else:
                ans += idx - right

        return ans


nums = [2,1,4,3,5]
k = 10

nums = [1,1,1]
k = 5

nums = [2,4,4,1,1,2]
k = 10

solution = Solution()
print(solution.countSubarrays(nums, k))
