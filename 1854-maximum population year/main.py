class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        # pre-process
        events = list()
        for log in logs:
            events.append((log[0], 1))
            events.append((log[1], -1))
        events = sorted(events)

        # process
        maxi = float('-inf')
        population = 0
        ans = ""
        for event in events:
            population += event[1]
            if population > maxi:
                maxi = population
                ans = event[0]
        return ans


logs = [[1993, 1999], [2000, 2010]]

solution = Solution()
print(solution.maximumPopulation(logs))
