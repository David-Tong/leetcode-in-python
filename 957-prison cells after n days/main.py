class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        # pre-process
        L = len(cells)

        # help function
        # transfer - transfer to the next day
        def transfer(cells):
            nxt_cells = [0] * L
            for x in range(L):
                if 0 < x < L - 1:
                    nxt_cells[x] = 1 - cells[x - 1] ^ cells[x + 1]
            return nxt_cells

        # key
        def key(cells):
            return "".join([str(_) for _ in cells])

        # process
        # calculate period
        from collections import defaultdict
        id, ids = key(cells), defaultdict(int)
        period, periods = 0, list()
        while id not in ids:
            ids[id] = period
            periods.append(cells)
            # print(period, id, cells)
            cells = transfer(cells)
            id = key(cells)
            # print(period + 1, id, cells)
            period += 1

        period -= ids[id]
        offset = ids[id]

        # print(period, offset)
        mod = (n - offset) % period
        # print(mod)
        ans = periods[offset + mod]
        return ans


cells = [0,1,0,1,1,0,0,1]
n = 7

cells = [1,0,0,1,0,0,1,0]
n = 1000000000

cells = [1,0,0,1,0,0,1,0]
n = 25

solution = Solution()
print(solution.prisonAfterNDays(cells, n))
