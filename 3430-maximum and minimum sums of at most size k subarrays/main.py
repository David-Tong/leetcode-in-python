class Solution(object):
    def minMaxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        # print(nums)

        # use monotonic stack to count the maxis and minis range
        # count maxis range
        # maxis[idx][0] - the most right index use nums[idx] as maxi
        # maxis[idx][1] - the most left index use nums[idx] as maxi
        # from left to right
        stack = list()
        maxis = [[-1, -1] for _ in range(L)]
        for x in range(L):
            # handle the case like nums = [2, 2], k = 2
            # we have to define a direction for equal case
            while stack and stack[-1][0] <= nums[x]:
                num, idx = stack.pop()
                maxis[idx][1] = x - 1
            stack.append((nums[x], x))
        while stack:
            num, idx = stack.pop()
            maxis[idx][1] = L - 1

        # from right to left
        for x in range(L - 1, -1, -1):
            # handle the case like nums = [2, 2], k = 2
            # we have to define a direction for equal case
            while stack and stack[-1][0] < nums[x]:
                num, idx = stack.pop()
                maxis[idx][0] = x + 1
            stack.append((nums[x], x))
        while stack:
            num, idx = stack.pop()
            maxis[idx][0] = 0

        # print(maxis)
        maxis = [[(max(idx - k + 1, maxi[0]), idx),(idx, min(idx + k - 1, maxi[1]))] for idx, maxi in enumerate(maxis)]
        # print(maxis)

        # count minis range
        # minis[idx][0] - the most right index use nums[idx] as mini
        # minis[idx][1] - the most left index use nums[idx] as mini
        # from left to right
        stack = list()
        minis = [[-1, -1] for _ in range(L)]
        for x in range(L):
            # handle the case like nums = [2, 2], k = 2
            # we have to define a direction for equal case
            while stack and stack[-1][0] >= nums[x]:
                num, idx = stack.pop()
                minis[idx][1] = x - 1
            stack.append((nums[x], x))
        while stack:
            num, idx = stack.pop()
            minis[idx][1] = L - 1

        # from right to left
        for x in range(L - 1, -1, -1):
            # handle the case like nums = [2, 2], k = 2
            # we have to define a direction for equal case
            while stack and stack[-1][0] > nums[x]:
                num, idx = stack.pop()
                minis[idx][0] = x + 1
            stack.append((nums[x], x))
        while stack:
            num, idx = stack.pop()
            minis[idx][0] = 0

        # print(minis)
        minis = [[(max(idx - k + 1, mini[0]), idx), (idx,  min(idx + k - 1, mini[1]))] for idx, mini in enumerate(minis)]
        # print(minis)

        # process
        # help function
        # count - count the number of subarray with the size <= k and including nums[x]
        """
        l, l, i, r, r, r

        the number of subarray 3 * 4 = 12
        i; 
        l, i; i, r;
        l, l, i; l, i, r; i, r, r;
        l, l, i, r; l, i, r, r; i, r, r, r;
        l, l, i, r, r; l, i, r, r, r; 
        l, l, i, r, r, r;
        
        1 + 2 + 3 + 3 + 2 + 1 = 12
        
        the number of subarray in the range [left, right] with size larger than k
        1 + 2 + ... + (right - left + 1) - k
        
        in the above case, right = 5, left = 0 right - left + 1 = 6 
        k = 3
        u = (right - left + 1) - k = 6 - 3 = 3 
        1 + 2 + 3
        u (u + 1) // 2 = 3 * 4 // 2 = 6 
        """
        def count(mami):
            left, idx = mami[0]
            idx, right = mami[1]

            # the total number of subarray in the range [left, right]
            total = (idx - left + 1) * (right - idx + 1)

            # the number of subarray with size larger than k
            sub = 0
            u = (right - left + 1) - k
            if u > 0:
                sub = u * (u + 1) // 2

            return total - sub

        ans = 0
        for x in range(L):
            ans += count(maxis[x]) * nums[x]
            # print(nums[x], count(maxis[x]))
            ans += count(minis[x]) * nums[x]
            # print(nums[x], count(minis[x]))
        ans = int(ans)
        return ans


nums = [1,2,3]
k = 2

nums = [1,4,2,3]
k = 2

nums = [1,-3,1]
k = 2

nums = [1,4,2,3]
k = 3

nums = [1,4,2,3,5]
k = 3

nums = [-7, -7]
k = 2

nums = [2, 2]
k = 2

nums = [10,-20,1,3]
k = 1

"""
from random import randint
nums = [randint(-1 * 10 ** 6, 10 ** 6) for _ in range(8 * 10 * 4)]
print(nums)
k = 34567
"""

solution = Solution()
print(solution.minMaxSubarraySum(nums, k))
