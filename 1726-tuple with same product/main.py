class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(int)
        for x in range(L):
            for y in range(x + 1, L):
                product = nums[x] * nums[y]
                dicts[product] += 1

        # process
        ans = 0
        for product in dicts:
            if dicts[product] > 1:
                combinations = dicts[product] * (dicts[product] - 1) // 2
                ans += combinations * 8
        return ans


nums = [2,3,4,6]
nums = [1,2,4,5,10]
nums = [2,4,8,16,32]

solution = Solution()
print(solution.tupleSameProduct(nums))

