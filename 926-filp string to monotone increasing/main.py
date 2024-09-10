class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        zeros = [0] * N
        ones = [0] * N

        # get zeros after it
        for x in range(N - 1, -1, -1):
            if s[x] == "0":
                if x == N - 1:
                    zeros[x] = 1
                else:
                    zeros[x] = zeros[x + 1] + 1
            else:
                if x == N - 1:
                    pass
                else:
                    zeros[x] = zeros[x + 1]

        # get ones before it
        for x in range(N):
            if s[x] == "1":
                if x == 0:
                    ones[x] = 1
                else:
                    ones[x] = ones[x - 1] + 1
            else:
                if x == 0:
                    pass
                else:
                    ones[x] = ones[x - 1]

        for x in range(N):
            if s[x] == "0":
                zeros[x] -= 1
            elif s[x] == "1":
                ones[x] -= 1

        ans = float("inf")
        for x in range(N):
            ans = min(ans, ones[x] + zeros[x])
        return ans


s = "00110"
s = "010110"
s = "00011000"
s = "0101010101"
s = "10101010101"
#s = "1"

solution = Solution()
print(solution.minFlipsMonoIncr(s))
