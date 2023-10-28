class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        # pre-process
        L = len(colors)

        alice_intervals = list()
        bob_intervals = list()

        alice_interval = list()
        bob_interval = list()

        for idx, color in enumerate(colors):
            if color == "A":
                if idx == 0:
                    alice_interval.append(idx)
                elif colors[idx - 1] == "B":
                    alice_interval.append(idx)
                    bob_interval.append(idx - 1)
                    bob_intervals.append(bob_interval)
                    bob_interval = list()

            elif color == "B":
                if idx == 0:
                    bob_interval.append(idx)
                elif colors[idx - 1] == "A":
                    bob_interval.append(idx)
                    alice_interval.append(idx - 1)
                    alice_intervals.append(alice_interval)
                    alice_interval = list()

        if colors[-1] == "A":
            alice_interval.append(L - 1)
            alice_intervals.append(alice_interval)
        elif colors[-1] == "B":
            bob_interval.append(L - 1)
            bob_intervals.append(bob_interval)

        # calculate turns
        alices = 0
        for interval in alice_intervals:
            alices += max(0, interval[1] - interval[0] - 1)

        bobs = 0
        for interval in bob_intervals:
            bobs += max(0, interval[1] - interval[0] - 1)

        return True if alices > bobs else False


colors = "AAABABB"
colors = "AA"
colors = "ABBBBBBBAAA"
colors = "B"
colors = "AAABBBBBBAAAAAAAABABABBAAAABBAAAB"

solution = Solution()
print(solution.winnerOfGame(colors))
