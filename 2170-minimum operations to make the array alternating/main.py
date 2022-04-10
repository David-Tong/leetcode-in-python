class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        from collections import defaultdict
        evens = defaultdict(int)
        odds = defaultdict(int)
        for x in range(len(nums)):
            if x % 2 == 0:
                evens[nums[x]] += 1
            else:
                odds[nums[x]] += 1

        evens_num = len(nums) // 2 + len(nums) % 2
        odds_num = len(nums) // 2
        for even in evens:
            evens[even] = evens_num - evens[even]
        for odd in odds:
            odds[odd] = odds_num - odds[odd]

        evens_nums = sorted(evens, key=lambda x : (evens[x]))
        odds_nums = sorted(odds, key=lambda x : (odds[x]))

        #"""
        print(evens_nums)
        print(evens)
        print(odds_nums)
        print(odds)
        #"""

        ans = float("inf")
        for evens_num in evens_nums[:2]:
            for odds_num in odds_nums[:2]:
                if evens_num != odds_num:
                    ans = min(ans, evens[evens_num] + odds[odds_num])
        if ans == float("inf"):
            return len(nums) // 2
        return ans


nums = [3, 1, 3, 2, 4, 3]
nums = [1, 2, 2, 2, 2]
nums = [1, 1, 1, 1, 1]
nums = [1, 2]
nums = [2, 3, 4, 1, 4, 2, 2, 2]
nums = [1, 3, 4, 3, 3, 2, 3, 3, 2, 2, 3]
nums = [2, 2, 2, 2, 2]
nums = [2, 2]

solution = Solution()
print(solution.minimumOperations(nums))

