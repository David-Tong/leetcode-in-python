class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        # pre-process
        L = len(nums)
        sort = sorted(nums[:k])

        # process
        # helper function
        # median
        def median():
            if k % 2 == 0:
                return (sort[k // 2 - 1] + sort[k // 2]) * 1.0 / 2
            else:
                return sort[k // 2]

        from bisect import bisect_left
        ans = list()
        ans.append(median())
        for x in range(k, L):
            # remove the most left element
            idx = bisect_left(sort, nums[x - k])
            sort.pop(idx)

            # add new element
            idx = bisect_left(sort, nums[x])
            sort.insert(idx, nums[x])

            # update answer
            ans.append(median())
        return ans


nums = [1,3,-1,-3,5,3,6,7]
k = 3

nums = [1,2,3,4,2,3,1,4,2]
k = 3

from random import randint
nums = [randint(-1 * 2 ** 31, 1 * 2 ** 31) for _ in range(10 ** 5)]
print(nums)
k = 5000

solution = Solution()
# print(solution.medianSlidingWindow(nums, k))
