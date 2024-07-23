class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        # pre-process
        L = len(aliceValues)

        values = list()
        for x in range(L):
            values.append([aliceValues[x] + bobValues[x], x])
        values = sorted(values, reverse=True)

        # process
        alice_points = 0
        bob_points = 0

        for x in range(L):
            if x % 2 == 0:
                alice_points += aliceValues[values[x][1]]
            else:
                bob_points += bobValues[values[x][1]]

        if alice_points > bob_points:
            return 1
        elif alice_points == bob_points:
            return 0
        else:
            return -1


aliceValues = [1,3]
bobValues = [2,1]

aliceValues = [1,2]
bobValues = [3,1]

aliceValues = [2,4,3]
bobValues = [1,6,7]

solution = Solution()
print(solution.stoneGameVI(aliceValues, bobValues))
