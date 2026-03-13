class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # init dict
        from collections import defaultdict
        init_even_dict, init_odd_dict = defaultdict(int), defaultdict(int)
        for num in nums:
            if num % 2 == 0:
                init_even_dict[num] += 1
            else:
                init_odd_dict[num] += 1

        # process
        l = 1
        step = L - l
        idx = 0
        while step > 0:
            if l > 1:
                num = nums[L - l + 1]
                if num % 2 == 0:
                    init_even_dict[num] -= 1
                    if init_even_dict[num] == 0:
                        del init_even_dict[num]
                else:
                    init_odd_dict[num] -= 1
                    if  init_odd_dict[num] == 0:
                        del init_odd_dict[num]

            from copy import deepcopy
            even_dict, odd_dict = deepcopy(init_even_dict), deepcopy(init_odd_dict)
            while idx + step < L:
                if len(even_dict.keys()) == len(odd_dict.keys()):
                    ans = step + 1
                    return ans

                # update
                idx += 1
                if idx + step < L:
                    left = nums[idx - 1]
                    if left % 2 == 0:
                        even_dict[left] -= 1
                        if even_dict[left] == 0:
                            del even_dict[left]
                    else:
                        odd_dict[left] -= 1
                        if odd_dict[left] == 0:
                            del odd_dict[left]

                    right = nums[idx + step]
                    if right % 2 == 0:
                        even_dict[right] += 1
                    else:
                        odd_dict[right] += 1
            l += 1
            step = L - l
            idx = 0

        return 0


nums = [2,5,4,3]
nums = [3,2,2,5,4]
nums = [1,2,3,2]

"""
from random import randint
nums = [randint(1, 10) for _ in range(50)]
print(nums)
"""

nums = [9,13,11,10]

solution = Solution()
print(solution.longestBalanced(nums))
