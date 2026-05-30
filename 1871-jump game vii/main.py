class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        # pre-process
        L = len(s)

        # process
        # dp init
        # dp[x] = 1 - means index x is reachable
        dp = [0] * L
        dp[0] = 1

        # prefix sum array for dp, ps[i] = sum(dp[0..i])
        ps = [0] * L
        ps[0] = dp[0]

        # dp transfer
        # dp[x] - check if s[x] == '0' and if any dp[y] = 1 exists in [x - maxJump, x - minJump]
        for x in range(1, L):
            if s[x] == '0':
                left = max(0, x - maxJump)
                right = x - minJump
                if right >= 0:
                    # compute sum(dp[left..right]) using prefix sum
                    total = ps[right] - (ps[left - 1] if left > 0 else 0)
                    if total > 0:
                        dp[x] = 1

            # update prefix sum
            ps[x] = ps[x - 1] + dp[x]

        ans = dp[L - 1] == 1
        return ans


s = "011010"
minJump = 2
maxJump = 3

s = "01101110"
minJump = 2
maxJump = 3

import random
s = "".join(random.choice("01") for _ in range(10 ** 5))
minJump = 1
maxJump = 10 ** 5 - 1
print(s)

solution = Solution()
print(solution.canReach(s, minJump, maxJump))
