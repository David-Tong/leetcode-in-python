class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        L = len(colors)

        alices = 0
        bobs = 0
        alice_start = 0
        bob_start = 0

        # calculate turns
        for idx, color in enumerate(colors):
            if color == "A":
                if idx == 0:
                    alice_start = 0
                elif colors[idx - 1] == "B":
                    alice_start = idx
                    bobs += max(0, idx - 1 - bob_start - 1)
            elif color == "B":
                if idx == 0:
                    bob_start = 0
                elif colors[idx - 1] == "A":
                    bob_start = idx
                    alices += max(0, idx - 1 - alice_start - 1)

        if colors[-1] == "A":
            alices += max(0, L - 1 - alice_start - 1)
        elif colors[-1] == "B":
            bobs += max(0, L - 1 - bob_start - 1)

        return True if alices > bobs else False


colors = "AAABABB"
colors = "AA"
colors = "ABBBBBBBAAA"
colors = "B"
colors = "AAABBBBBBAAAAAAAABABABBAAAABBAAAB"
colors = "AAAABBBB"

solution = Solution()
print(solution.winnerOfGame(colors))
