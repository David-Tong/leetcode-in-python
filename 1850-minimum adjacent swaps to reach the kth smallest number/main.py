class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        # pre-process
        nums = [int(n) for n in num]
        L = len(num)

        # helper function
        from bisect import bisect_right
        def nextPermutation(nums):
            idx = L - 1
            digits = list()
            while idx > 0:
                digits.append(nums[idx])
                if nums[idx] > nums[idx - 1]:
                    target = int(nums[idx - 1])
                    idx2 = bisect_right(digits, target)
                    target2 = digits[idx2]
                    digits[idx2] = target
                    res = nums[:idx - 1] + [target2] + digits
                    return res
                idx -= 1
            raise ValueError("Next permutation doesn't exist")

        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]

        # process
        target = nums
        idx = 0
        while idx < k:
            target = nextPermutation(target)
            # print(target)
            idx += 1

        ans = 0
        for x in range(L):
            if nums[x] != target[x]:
                for y in range(x + 1, L):
                    if nums[y] == target[x]:
                        for z in range(y, x, -1):
                            swap(z, z - 1)
                            ans += 1
                        # print(nums)
                        break
        return ans


num = "5489355142"
k = 4

num = "11112"
k = 4

num = "00123"
k = 1

"""
import random
import string
num = "".join(random.choice(string.digits) for _ in range(20))
k = 3
print(num)
"""

num = "86127003039509847712"
k = 2

solution = Solution()
print(solution.getMinSwaps(num, k))
