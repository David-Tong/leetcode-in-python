class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        L = len(tokens)
        tokens = sorted(tokens)

        left = 0
        right = L - 1
        score = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            else:
                if score > 0 and tokens[left] < tokens[right]:
                    power += tokens[right]
                    score -= 1
                    right -= 1
                else:
                    break
        return score


tokens = [100]
power = 50

tokens = [100,200]
power = 150

tokens = [100,200,300,400]
power = 200

tokens = [10, 10, 10, 10, 10, 10, 1000]
power = 10

tokens = [10, 10, 10, 10, 10]
power = 30

"""
tokens = [10, 1000, 1000, 1000]
power = 10

tokens = []
power = 10

tokens = [0, 0, 0, 0, 0]
power = 0
"""

solution = Solution()
print(solution.bagOfTokensScore(tokens, power))
