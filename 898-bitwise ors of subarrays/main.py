class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # process
        # dp init
        # dp[x] - bitwise ors of all sub arrays end with arr[:x+1]
        curr = set()
        ans = set()

        # dp transfer
        # dp[x] = [c | arr[x] for c in dp[x - 1]] + arr[x]
        for num in arr:
            nxt = set()
            nxt.add(num)
            for c in curr:
                nxt.add(num | c)
            curr = nxt
            ans |= curr
        return len(ans)


arr = [0]
arr = [1,1,2]
arr = [1,2,4]
arr = [1,2,7,4]
arr = [1,2,4,7]

solution = Solution()
print(solution.subarrayBitwiseORs(arr))
