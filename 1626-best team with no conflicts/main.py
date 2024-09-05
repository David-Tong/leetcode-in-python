class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        L = len(scores)

        pairs = zip(ages, scores)
        pairs = sorted(pairs, key=lambda x: (x[0], x[1]))

        from collections import defaultdict
        players = defaultdict(list)
        for x in range(L):
            players[pairs[x][0]].append(pairs[x][1])
        print(players)

        dp = defaultdict(int)
        dp[0] = 0
        for age in sorted(players.keys()):
            curr = defaultdict(int)
            for kscore in sorted(dp.keys()):
                total = 0
                for score in players[age]:
                    if score >= kscore:
                        total += score
                        curr[score] = max(curr[score], dp[kscore] + total)
            for cscore in curr:
                dp[cscore] = curr[cscore]

        return max(dp.values())

scores = [1,3,5,10,15]
ages = [1,2,3,4,5]

scores = [4,5,6,5]
ages = [2,1,2,1]

scores = [1,2,3,5]
ages = [8,9,10,1]

scores = [1,3,7,3,2,4,10,7,5]
ages = [4,5,2,1,1,2,4,1,4]

solution = Solution()
print(solution.bestTeamScore(scores, ages))
