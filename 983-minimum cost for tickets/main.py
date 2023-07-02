class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        def get_cost(day):
            if day in self.cache:
                return self.cache[day]

            if day <= 0:
                return 0

            if day not in days:
                from bisect import bisect_left
                idx = bisect_left(days, day)
                if idx == 0:
                    return get_cost(0)
                else:
                    return get_cost(days[idx - 1])
            else:
                cost = min(get_cost(day - 1) + costs[0], min(get_cost(day - 7) + costs[1], get_cost(day - 30) + costs[2]))
                self.cache[day] = cost
                return cost

        from collections import defaultdict
        self.cache = defaultdict(int)
        return get_cost(days[-1])


days = [1,4,6,7,8,20]
costs = [2,7,15]

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

days = [1,2,4,5,6,11,15,17,18,22,25]
costs = [2,5,11]

days = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99]
costs = [9,38,134]

days = [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
costs = [3,13,45]

solution = Solution()
print(solution.mincostTickets(days, costs))
