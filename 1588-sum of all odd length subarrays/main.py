class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr) + 1
        prefix_sum = [0] * N
        for x in range(1, N):
            prefix_sum[x] = prefix_sum[x-1] + arr[x-1]

        ans = 0
        for x in range(N):
            for y in range(x+1, N):
                if (y - x) % 2 == 1:
                    ans += prefix_sum[y] - prefix_sum[x]
        return ans


arr = [1,4,2,5,3]
arr = [1,2]
arr = [10,11,12]
arr = [1]

solution = Solution()
print(solution.sumOddLengthSubarrays(arr))
