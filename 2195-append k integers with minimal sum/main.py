class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)
        # print(nums)

        # helper
        # total
        def total(left, right):
            if left >= right:
                res = 0
            else:
                res = (right - 1) * right // 2 - left * (left + 1) // 2
            # print(left, right, res)
            return res

        # process
        idx = 0
        curr = 0
        gap = k
        ans = 0
        while idx < L and gap > 0:
            # print("gap", gap, curr, nums[idx])
            if gap < nums[idx] - 1 - curr:
                ans += total(curr, curr + gap + 1)
                gap = 0
            else:
                ans += total(curr, nums[idx])
                if nums[idx] > curr:
                    gap -= nums[idx] - 1 - curr
            curr = nums[idx]
            idx += 1

        if gap > 0:
            ans += total(curr, curr + gap + 1)
        return ans


nums = [1,4,25,10,25]
k = 2

nums = [5,6]
k = 6

nums = [1,4,25,10,25]
k = 4

nums = [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
k = 35
k = 18

solution = Solution()
print(solution.minimalKSum(nums, k))
