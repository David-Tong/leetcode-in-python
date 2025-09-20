class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # conner case
        L = len(nums)
        if k == 1:
            return range(1, L - 1)

        # pre-process
        left = [0] * L
        count = 0
        for x in range(1, L):
            if nums[x] <= nums[x - 1]:
                if count == 0:
                    count += 1
                count += 1
            else:
                count = 0
            left[x] = count
        print(left)

        right = [0] * L
        count = 0
        for x in range(L - 2, -1, -1):
            if nums[x + 1] >= nums[x]:
                if count == 0:
                    count += 1
                count += 1
            else:
                count = 0
            right[x] = count
        print(right)

        # process
        ans = list()
        for x in range(k, L - k):
            if left[x - 1] >= k and right[x + 1] >= k:
                ans.append(x)
        return ans


nums = [2,1,1,1,3,4,1]
k = 2

"""
nums = [2,1,1,1,3,4,5]
k = 2

nums = [2,1,1,2]
k = 2

nums = [1,1,1,1,1,1,1,1,1]
k = 3

nums = [433,639679,267108,15179,14818,10492,8478,3160,2340,1506,1168,1167,600,523,152,132,111,51,736058,237085,943608,997519,997796,998643,999914,999922,999947,999971,999993,999997]
k = 10
"""

nums = [440043,276285,336957]
k = 1

solution = Solution()
print(solution.goodIndices(nums, k))
