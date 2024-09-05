class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        # pre-process
        offsets = {
            "2": 3,
            "3": 3,
            "4": 3,
            "5": 3,
            "6": 3,
            "7": 4,
            "8": 3,
            "9": 4,
        }

        MODULO = 10 ** 9 + 7

        # dp[x] - the number of texts for pressedKeys[:x + 1]
        L = len(pressedKeys)
        dp = [0] * (L + 1)
        dp[0] = 1

        # process
        for idx, key in enumerate(pressedKeys):
            for offset in range(offsets[key]):
                if idx - offset >= 0:
                    if offset == 0:
                        dp[idx + 1] += dp[idx]
                    else:
                        if pressedKeys[idx] == pressedKeys[idx - offset]:
                            dp[idx + 1] += dp[idx - offset]
                        else:
                            break
        return dp[L] % MODULO


pressedKeys = "22233"
pressedKeys = "222222222222222222222222222222222222"

solution = Solution()
print(solution.countTexts(pressedKeys))
