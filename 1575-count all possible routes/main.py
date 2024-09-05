class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        import sys
        sys.setrecursionlimit(4000)

        def doRoute(idx, remain_fuel):
            key = str(idx) + "-" + str(remain_fuel)
            if key in self.cache:
                return self.cache[key]

            routes = 0
            if remain_fuel < 0:
                return 0
            elif remain_fuel >= 0:
                if idx == finish:
                    routes += 1

            for next_idx, next_location in enumerate(locations):
                if idx != next_idx:
                    next_remain_fuel = remain_fuel - abs(next_location - locations[idx])
                    routes += doRoute(next_idx, next_remain_fuel)

            self.cache[key] = routes % MODULO
            return self.cache[key]

        from collections import defaultdict
        self.cache = defaultdict(int)

        return doRoute(start, fuel)


locations = [2,3,6,8,4]
start = 1
finish = 3
fuel = 5

locations = [4,3,1]
start = 1
finish = 0
fuel = 6

locations = [5,2,1]
start = 0
finish = 2
fuel = 3

locations = list()
from random import randint
for x in range(100):
    rand_num = randint(1, 10 ** 3)
    if rand_num not in locations:
        locations.append(rand_num)
start = 55
finish = 12
fuel = 200

solution = Solution()
print(solution.countRoutes(locations, start, finish, fuel))
