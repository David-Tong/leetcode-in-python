class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        import math
        M = int(math.log(max(nums)) / math.log(2)) + 1
        # print(M)
        N = len(nums)
        bins = [[0] * M for _ in range(N)]
        presums = [0] * M
        high = 0
        for x in range(N):
            idx = 0
            target = nums[x]
            while target:
                if target & 1:
                    high = max(high, idx)
                bins[x][idx] = target & 1
                presums[idx] = presums[idx] + (target & 1)
                target >>= 1
                idx += 1

        # print(presums)
        # print(bins)

        highs = list()
        for x in range(N):
            if bins[x][high] == 1:
                highs.append(x)
        # print(highs)

        # process
        # helper function
        # ors result of nums without idx'th element
        def ors(idx):
            res = 0
            for x in range(M):
                if presums[x] - bins[idx][x] > 0:
                    res += 2 ** x
            return res

        ans = 0
        for high in highs:
            ans = max(ans, ors(high) | nums[high] << k)
        return ans


nums = [12,9]
k = 1

nums = [8,1,2]
k = 2

solution = Solution()
print(solution.maximumOr(nums, k))
