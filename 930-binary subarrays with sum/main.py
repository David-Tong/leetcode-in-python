class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefixes = list()
        prefixes.append(0)
        for num in nums:
            prefixes.append(prefixes[-1] + num)

        ans = 0
        from collections import defaultdict
        dicts = defaultdict(int)
        for prefix in prefixes:
            if prefix - goal in dicts:
                ans += dicts[prefix - goal]
            dicts[prefix] += 1
        return ans


nums = [1,0,1,0,1]
goal = 2

nums = [0,0,0,0,0]
goal = 0

nums = [1]
goal = 1

solution = Solution()
print(solution.numSubarraysWithSum(nums, goal))
