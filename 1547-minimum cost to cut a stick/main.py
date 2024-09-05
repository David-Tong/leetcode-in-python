class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        L = len(cuts)

        # pre-process
        cuts = sorted(cuts)
        sticks = list()
        for x in range(L):
            if x == 0:
                sticks.append(cuts[x])
            else:
                sticks.append(cuts[x] - cuts[x - 1])
        sticks.append(n - cuts[-1])

        # presum
        presum = list()
        presum.append(0)
        for x in range(L + 1):
            presum.append(sticks[x] + presum[x])

        def cut(start, end):
            key = str(start) + "-" + str(end)
            if key in self.cache:
                return self.cache[key]

            if start + 1 == end:
                return 0

            mini = float("inf")
            for x in range(start + 1, end):
                mini = min(mini, cut(start, x) + cut(x, end) + presum[end] - presum[start])
            self.cache[key] = mini
            return mini

        from collections import defaultdict
        self.cache = defaultdict(int)

        return cut(0, L + 1)


n = 7
cuts = [1,3,4,5]

n = 9
cuts = [5,6,1,4,2]

n = 50000
cuts = [1,2,5,6,7,11,17,200,256,177,87,290,1000,1500,1800,1897,2000,2500,6000,10000,12000,25000,36000,42000,49000]

n = 50000
cuts = [1,2,5,6,7,11,17,200,256,177,87,290,1000,1500,1800,1897,2000,2500,3400,3900,6000,6500,6700,6900,10000,11000,12000,12345,12555,16700,18000,19000,20000,22000,22020,22025,24000,25000,27500,28000,30000,30002,30003,30005,30007,36000,42000,45000,45555,45666,45777,46899,49000]

soltuion = Solution()
print(soltuion.minCost(n, cuts))
