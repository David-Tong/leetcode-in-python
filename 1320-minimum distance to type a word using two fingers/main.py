class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        keyboard = {"A": (0, 0), "B": (0, 1), "C": (0, 2), "D": (0, 3), "E": (0, 4), "F": (0, 5),
                    "G": (1, 0), "H": (1, 1), "I": (1, 2), "J": (1, 3), "K": (1, 4), "L": (1, 5),
                    "M": (2, 0), "N": (2, 1), "O": (2, 2), "P": (2, 3), "Q": (2, 4), "R": (2, 5),
                    "S": (3, 0), "T": (3, 1), "U": (3, 2), "V": (3, 3), "W": (3, 4), "X": (3, 5),
                    "Y": (4, 0), "Z": (4, 1)}

        # helper function
        # get distance
        def getDistance(ch, other):
            if ch == "":
                return 0
            else:
                x, y = keyboard[ch]
                ox, oy = keyboard[other]
                return abs(x - ox) + abs(y - oy)

        # print(getDistance('A', 'K'))

        # dp init
        # dp[x][y][z] - the minimum distance to type word[:x + 1]
        L = len(word)
        C = 26
        from collections import defaultdict
        prev = defaultdict(dict)
        ch = word[0]
        prev[ch][''] = 0
        prev[''][ch] = 0

        # dp transfer
        for x in range(1, L):
            ch = word[x]
            dp = defaultdict(dict)
            # put the first finger on ch
            for first in prev:
                for second in prev[first]:
                    if ch not in dp:
                        dp[ch] = dict()
                    if second not in dp[ch]:
                        dp[ch][second] = float("inf")
                    dp[ch][second] = min(dp[ch][second], prev[first][second] + getDistance(first, ch))
            # put the second finger on ch
            for first in prev:
                for second in prev[first]:
                    if first not in dp:
                        dp[first] = dict()
                    if ch not in dp[first]:
                        dp[first][ch] = float("inf")
                    dp[first][ch] = min(dp[first][ch], prev[first][second] + getDistance(second, ch))
            # print(dp)
            prev = dp

        ans = float("inf")
        for first in dp:
            for second in dp[first]:
                ans = min(ans, dp[first][second])
        return ans


word = "CAKE"
word = "HAPPY"
word = "HELLOWORLDPIGLEETCODEHOWAREYOU"

"""
import random
import string
word = "".join(random.choice(string.ascii_uppercase) for _ in range(150))
print(word)
"""

soluion = Solution()
print(soluion.minimumDistance(word))
