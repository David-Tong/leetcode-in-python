class Solution(object):
    def maxBalancedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        xor = 0
        balance = 0
        key = "{}&{}".format(xor, balance)
        dicts[key] = -1
        ans = 0
        for idx, num in enumerate(nums):
            xor ^= num
            if num % 2 == 0:
                balance += 1
            else:
                balance -= 1
            key = "{}&{}".format(xor, balance)
            if key in dicts:
                ans = max(ans, idx - dicts[key])
            else:
                dicts[key] = idx
            # print(dicts)
        return ans


nums = [3,1,3,2,0]
nums = [3,2,8,5,4,14,9,15]
nums = [0]

from random import randint
nums = [randint(0, 10 ** 5) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.maxBalancedSubarray(nums))
