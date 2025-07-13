class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        xors = list()
        for x in range(L - 1, -1, -1):
            if x == L - 1:
                xors.append(nums[x])
            else:
                xors.append(xors[-1] | nums[x])
        xors = xors[::-1]

        B = len(bin(max(nums))) - 2
        presum = [[0] * B for _ in range(L + 1)]
        for x in range(L):
            for idx in range(B):
                presum[x + 1][idx] = presum[x][idx]
            idx = 0
            num = nums[x]
            while num:
                presum[x + 1][idx] = presum[x][idx] + (num & 1)
                num >>= 1
                idx += 1

        # process
        # xor - the xor sum from start to target
        def xor(start, target):
            res = 0
            for idx in range(B):
                if presum[target + 1][idx] - presum[start][idx] > 0:
                    res += 2 ** idx
            return res

        ans = list()
        for x in range(L):
            left, right = x, L - 1
            while left + 1 < right:
                middle = (left + right) // 2
                if xor(x, middle) == xors[x]:
                    right = middle
                else:
                    left = middle + 1
            if xor(x, left) == xors[x]:
                ans.append(left - x + 1)
            else:
                ans.append(right - x + 1)
        return ans


nums = [1,0,2,1,3]
nums = [1,2]
nums = [2,1]

nums = [_ for _ in range(100000)]

solution = Solution()
print(solution.smallestSubarrays(nums))
