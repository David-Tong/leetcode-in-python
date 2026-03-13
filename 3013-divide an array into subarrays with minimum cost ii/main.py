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
        M = k - 1

        # process
        from sortedcontainers import SortedList
        topk = SortedList()
        rest = SortedList()

        idx = 1
        step = 0
        while step <= dist:
            topk.add(nums[idx + step])
            if len(topk) > M:
                rest.add(topk.pop())
            step += 1
        mini = sum(topk)
        temp = mini

        """
        print(topk)
        print(rest)
        print(mini)
        """
        while idx + dist < L - 1:
            # update left
            left = nums[idx]
            idx_left = topk.bisect_left(left)
            if idx_left == M or topk[idx_left] != left:
                # left not in top k
                rest.remove(left)
            else:
                # left in top k
                topk.remove(left)
                temp -= left

            # update right
            idx += 1
            right = nums[idx + dist]
            rest.add(right)
            if len(topk) < M:
                to_add = rest[0]
                topk.add(rest.pop(0))
                temp += to_add
            else:
                if rest[0] < topk[-1]:
                    to_add = rest[0]
                    to_remove = topk[-1]
                    topk.pop()
                    topk.add(to_add)
                    rest.pop(0)
                    rest.add(to_remove)
                    temp += to_add
                    temp -= to_remove

            # update
            mini = min(mini, temp)

            """
            print(topk)
            print(rest)
            print(mini)
            """

        # post-process
        ans = nums[0] + mini
        return ans


"""
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

"""
from random import randint
nums = [randint(1, 10 ** 3) for _ in range(30)]
print(nums)
k = 5
dist = 10
"""

"""
nums = [36,28,42,36,39,13,24,3,32,16,11,43,21,40,34,49,29,20,34,34,8,3,41,6,46,5,35,5,47,2]
k = 25
dist = 26
"""

""""
nums = [908, 334, 370, 842, 878, 823, 838, 199, 833, 515, 976, 757, 829, 823, 695, 237, 461, 627, 279, 710, 482, 569, 360, 615, 545, 89, 395, 881, 711, 757]
k = 5
dist = 10
"""

from random import randint
nums = [randint(1, 10 ** 3) for _ in range(10 ** 5)]
print(nums)
k = 20000
dist = 25000

solution = Solution()
print(solution.minimumCost(nums, k, dist))
