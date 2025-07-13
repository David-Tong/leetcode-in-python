class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        # pre-process
        players, trainers = sorted(players), sorted(trainers)

        # process
        idx, idx2 = 0, 0
        M, N = len(players), len(trainers)

        ans = 0
        while idx < M and idx2 < N:
            if players[idx] <= trainers[idx2]:
                ans += 1
                idx += 1
                idx2 += 1
            else:
                idx2 += 1
        return ans


players = [4,7,9]
trainers = [8,2,5,8]

players = [1,1,1]
trainers = [10]

players = [10]
trainers = [1]

players = [1,1]
trainers = [2,2,2]

solution = Solution()
print(solution.matchPlayersAndTrainers(players, trainers))
