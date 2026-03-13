class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)

        # helper function
        def search(stride, start, end):
            maxi = 0
            idx = start
            while idx + stride <= end:
                maxi = max(maxi, presums[idx + stride] - presums[idx])
                idx += 1
            return maxi

        # process
        ans = 0

        idx = 0
        while idx + firstLen <= L:
            maxi = presums[idx + firstLen] - presums[idx]
            maxi2 = max(search(secondLen, 0, idx - 1), search(secondLen, idx + firstLen, L))
            idx += 1
            ans = max(ans, maxi + maxi2)
        return ans


nums = [0,6,5,2,2,5,1,9,4]
firstLen = 1
secondLen = 2

nums = [3,8,1,3,2,1,8,9,0]
firstLen = 3
secondLen = 2

nums = [2,1,5,6,0,9,5,0,3,8]
firstLen = 4
secondLen = 3

solution = Solution()
print(solution.maxSumTwoNoOverlap(nums, firstLen, secondLen))