class Solution(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        from sortedcontainers import SortedList
        sl = SortedList()

        idx = 1
        step = 0
        while step <= dist:
            sl.add(nums[idx + step])
            step += 1
        mini = sum(sl[:k - 1])

        ans = mini
        # print(sl)
        # print(mini)
        while idx + dist < L - 1:
            # update left
            sl.remove(nums[idx])

            # update right
            idx += 1
            sl.add(nums[idx + dist])

            # update
            mini = sum(sl[:k - 1])
            ans = min(ans, mini)
            # print(sl)
            # print(mini)

        # post-process
        ans += nums[0]
        return ans


nums = [1,3,2,6,4,2]
k = 3
dist = 3

nums = [10,1,2,2,2,1]
k = 4
dist = 3

nums = [10,8,18,9]
k = 3
dist = 1

"""
from random import randint
nums = [randint(1, 10 ** 3) for _ in range(10)]
print(nums)
k = 3
dist = 5
"""

"""
nums = [518, 984, 400, 324, 28, 414, 328, 283, 458, 871]
k = 3
dist = 5
"""

solution = Solution()
print(solution.minimumCost(nums, k, dist))
