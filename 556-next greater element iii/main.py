class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def swap(nums, idx, idx2):
            tmp = nums[idx]
            nums[idx] = nums[idx2]
            nums[idx2] = tmp

        nums = [_ for _ in str(n)]
        N = len(nums)

        # find the end of decreasing sequence
        start = -1
        for x in range(N - 1, 0, -1):
            if nums[x] > nums[x - 1]:
                start = x - 1
                break
        if start == -1:
            return -1

        # find the digit right larger than nums[start]
        replace = -1
        for x in range(start + 1, N):
            if nums[x] <= nums[start]:
                replace = x - 1
                break
        swap(nums, start, replace)

        # sort the decreasing sequence to an increasing sequence
        nums = nums[:start + 1] + sorted(nums[start + 1:])
        ans = int("".join(nums))

        if ans > 2 ** 31 - 1 or ans < -1 * 2 ** 31:
            return -1
        else:
            return ans

n = 12
n = 21

n = 778135
#n = 2147483486
#n = 2147483476

n = 7784532

solution = Solution()
print(solution.nextGreaterElement(n))
