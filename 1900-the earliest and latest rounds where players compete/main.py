from compiler.ast import LeftShift

from setuptools.msvc import winreg


class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        # pre-process
        def key(players):
            return "-".join([str(player) for player in players])

        # process
        self.mini, self.maxi = float("inf"), 0
        from collections import defaultdict
        self.cache = defaultdict(bool)

        # dfs
        bests = [firstPlayer, secondPlayer]
        def arrange(round, idx, players, winners):
            L = len(players)
            left, right = idx, L - 1 - idx
            if left < right:
                if players[left] in bests:
                    if players[right] in bests:
                        self.mini = min(self.mini, round)
                        self.maxi = max(self.maxi, round)
                    else:
                        arrange(round, idx + 1, players, winners + [players[left]])
                else:
                    if players[right] in bests:
                        arrange(round, idx + 1, players, winners + [players[right]])
                    else:
                        arrange(round, idx + 1, players, winners + [players[left]])
                        arrange(round, idx + 1, players, winners + [players[right]])
            else:
                if left == right:
                    winners.append(players[left])
                players = sorted(winners)
                k = key(players)
                if k not in self.cache:
                    self.cache[k] = True
                    # print(k)
                    arrange(round + 1, 0, players, list())

        players = [x + 1 for x in range(n)]
        arrange(1, 0, players, list())

        ans = [self.mini, self.maxi]
        return ans


n = 11
firstPlayer = 2
secondPlayer = 4

n = 5
firstPlayer = 1
secondPlayer = 3

n = 5
firstPlayer = 1
secondPlayer = 5

n = 28
firstPlayer = 2
secondPlayer = 14

n = 28
firstPlayer = 13
secondPlayer = 17

solution = Solution()
print(solution.earliestAndLatest(n, firstPlayer, secondPlayer))
