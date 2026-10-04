class Solution(object):
    def minRemovals(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # pre-process
        n_target = target
        for num in nums:
            n_target = n_target ^ num

        # process
        from collections import defaultdict
        dicts = defaultdict(int)
        dicts[0] = 0

        for num in nums:
            n_dicts = defaultdict(int)
            for key in dicts:
                # don't xor num
                if key in n_dicts:
                    n_dicts[key] = min(n_dicts[key], dicts[key])
                else:
                    n_dicts[key] = dicts[key]
                # xor num
                n_key = key ^ num
                if n_key in n_dicts:
                    n_dicts[n_key] = min(n_dicts[n_key], dicts[key] + 1)
                else:
                    n_dicts[n_key] = dicts[key] + 1
            dicts = n_dicts

        if n_target in dicts:
            ans = dicts[n_target]
        else:
            ans = -1
        return ans


nums = [1,2,3]
target = 2

nums = [2,4]
target = 1

nums = [7]
target = 7

from random import randint
nums = [randint(0, 10 ** 4) for _ in range(40)]
target = randint(0, 10 ** 4)
print(nums)
print(target)

solution = Solution()
print(solution.minRemovals(nums, target))
