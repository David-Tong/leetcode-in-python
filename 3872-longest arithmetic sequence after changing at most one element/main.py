class Solution(object):
    def longestArithmetic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # helper function
        # res[x][0] - the length of arithmetic sequence ended with x
        # res[x][1] = the delta
        def process(nums, reverse=False):
            if reverse:
                nums = list(reversed(nums))
            res = [[0] * 2 for _ in range(L)]
            idx = 0
            while idx < L:
                if idx == 0:
                    res[idx][0] = 1
                    res[idx][1] = float("inf")
                elif idx == 1:
                    res[idx][0] = 2
                    res[idx][1] = nums[idx] - nums[idx - 1]
                else:
                    if nums[idx] - nums[idx - 1] == nums[idx - 1] - nums[idx - 2]:
                        res[idx][0] = res[idx - 1][0] + 1
                    else:
                        res[idx][0] = 2
                    res[idx][1] = nums[idx] - nums[idx - 1]
                idx += 1
            if reverse:
                res = list(reversed(res))
            return res

        lefts = process(nums)
        rights = process(nums, reverse=True)

        # print(lefts)
        # print(rights)

        # process
        # helper function
        # return the maximum arithmetic sequence we may achieve by replace the nums[idx]
        def check(idx):
            res = 1
            if idx == 0:
                res += rights[idx + 1][0]
                return res
            elif idx == L - 1:
                res += lefts[idx - 1][0]
                return res
            else:
                # check if we may merge left and right
                # nums[idx] - nums[idx - 1] = nums[idx + 1] - nums[idx]
                # nums[idx] = (nums[idx + 1] + nums[idx - 1]) // 2
                # 8, 6, 7, 8, 6
                # go to replace 7, (8 + 6) // 2 = 7 doesn't equal to previous delta
                if lefts[idx - 1][1] == -1 * rights[idx + 1][1]:
                    target = (nums[idx + 1] + nums[idx - 1]) // 2
                    if target - nums[idx - 1] == lefts[idx - 1][1]:
                        res += lefts[idx - 1][0] + rights[idx + 1][0]
                        return res

                if lefts[idx - 1][0] > rights[idx + 1][0]:
                    res += lefts[idx - 1][0]
                    target = lefts[idx - 1][1] + nums[idx - 1]
                    if nums[idx + 1] - target == lefts[idx - 1][1]:
                        res += 1
                elif lefts[idx - 1][0] < rights[idx + 1][0]:
                    res += rights[idx + 1][0]
                    target = nums[idx + 1] + rights[idx + 1][1]
                    if nums[idx - 1] - target == rights[idx + 1][1]:
                        res += 1
                else:
                    res += lefts[idx - 1][0]
                    target = lefts[idx - 1][1] + nums[idx - 1]
                    if nums[idx + 1] - target == lefts[idx - 1][1]:
                        res += 1
                    else:
                        target = nums[idx + 1] + rights[idx + 1][1]
                        if nums[idx - 1] - target == rights[idx + 1][1]:
                            res += 1
                return res

        # print(check(3))

        # search
        ans = 0
        idx = 0
        while idx < L:
            ans = max(ans, check(idx))
            idx += 1
        return ans


nums = [9,7,5,10,1]
nums = [1,2,6,7]
nums = [9,7,5,10,2,4]
nums = [12,10,8,7,4,2]
nums = [10,8,6,7,4,2]
nums = [79734,13414,52866,11223,46264,42963]
nums = [100,99,8,1,4,2]

"""
from random import randint
nums = [randint(1, 10 ** 5) for _ in range(10 ** 5)]
print(nums)
"""

solution = Solution()
print(solution.longestArithmetic(nums))

