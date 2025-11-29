class Solution(object):
    def minimumOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        gap = [x - y for x, y in zip(target, nums)]
        print(gap)

        # process
        ans = 0
        pivot = 0
        for x in range(L):
            if gap[x] > pivot:
                ans += gap[x] - pivot
            pivot = gap[x]
        if pivot < 0:
            ans -= pivot
        return ans


nums = [3,5,1,2]
target = [4,6,2,4]

nums = [1,3,2]
target = [2,1,4]

from random import randint
nums = [randint(1, 10 ** 8) for _ in range(10 ** 3)]
target = [randint(1, 10 ** 8) for _ in range(10 ** 3)]
print(nums)
print(target)

nums = [1,1,3,4]
target = [4,1,3,2]

solution = Solution()
print(solution.minimumOperations(nums, target))
