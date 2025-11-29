class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        # pre-process
        nums = list()
        for x in range(n):
            nums.append(start + x * 2)

        # process
        ans = nums[0]
        for x in range(1, n):
            ans ^= nums[x]
        return ans


n = 5
start = 0

n = 4
start = 3

solution = Solution()
print(solution.xorOperation(n, start))
