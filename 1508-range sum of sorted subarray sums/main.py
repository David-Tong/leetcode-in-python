class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        presum = list()
        presum.append(0)
        for num in nums:
            presum.append(presum[-1] + num)

        sums = list()
        for x in range(n + 1):
            for y in range(x + 1, n + 1):
                sums.append(presum[y] - presum[x])

        sums = sorted(sums)
        ans = sum(sums[left - 1:right])
        return ans % MODULO


nums = [1,2,3,4]
n = 4
left = 1
right = 5

nums = [1,2,3,4]
n = 4
left = 3
right = 4

nums = [1,2,3,4]
n = 4
left = 1
right = 10

nums = [2]
n = 1
left = 1
right = 1

nums = [1,2,3,4,7,9,10,11]
n = 8
left = 1
right =15

solution = Solution()
print(solution.rangeSum(nums, n, left, right))

