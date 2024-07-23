class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L = len(nums)

        def dfs(idx, state):
            if idx == L:
                return 1

            conflict = False
            for x in range(idx):
                if (state >> x) & 1 and abs(nums[idx] - nums[x]) == k:
                    conflict = True
                    break

            ans = 0
            if not conflict:
                ans += dfs(idx + 1, state + (1 << idx))
            ans += dfs(idx + 1, state)
            return ans

        return dfs(0, 0) - 1


nums = [2,4,6]
k = 2

solution = Solution()
print(solution.beautifulSubsets(nums, k))
