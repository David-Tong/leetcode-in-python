class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        N = len(secret)
        # digits[x][0] - number of x in secret, digits[x][1] - number of x in guess
        digits = [[0] * 2 for _ in range(10)]
        bulls = 0
        for x in range(N):
            if secret[x] != guess[x]:
                digits[int(secret[x])][0] += 1
                digits[int(guess[x])][1] += 1
            else:
                bulls += 1

        cows = 0
        for x in range(10):
            cows += min(digits[x][0], digits[x][1])

        ans = str(bulls) + "A" + str(cows) + "B"
        return ans


secret = "1807"
guess = "7810"

secret = "1123"
guess = "0111"

solution = Solution()
print(solution.getHint(secret, guess))
