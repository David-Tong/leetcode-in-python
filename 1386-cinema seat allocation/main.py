class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = 11
        from collections import defaultdict
        reserved = defaultdict(list)

        for reservedSeat in reservedSeats:
            row, seat = reservedSeat
            if row not in reserved:
                reserved[row] = [0] * L
            reserved[row][seat] = 1

        # helper function
        def check(row):
            res = 0
            # check seat from 2
            seat = 2
            arranged = True
            while seat <= 5:
                if reserved[row][seat] == 1:
                    arranged = False
                    break
                seat += 1

            if arranged:
                res += 1
                arranged = False
            else:
                seat = 4
                arranged = True
                while seat <= 7:
                    if reserved[row][seat] == 1:
                        arranged = False
                        break
                    seat += 1
                if arranged:
                    res += 1

            if not arranged:
                seat = 6
                arranged = True
                while seat <= 9:
                    if reserved[row][seat] == 1:
                        arranged = False
                        break
                    seat += 1
                if arranged:
                    res += 1

            return res

        # process
        rows = len(reserved)
        ans = (n - rows) * 2
        for row in reserved:
            ans += check(row)
        return ans


n = 3
reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]

n = 2
reservedSeats = [[2,1],[1,8],[2,6]]

n = 4
reservedSeats = [[4,3],[1,4],[4,6],[1,7]]

n = 2
reservedSeats = [[1,6],[1,8],[1,3],[2,3],[1,10],[1,2],[1,5],[2,2],[2,4],[2,10],[1,7],[2,5]]

solution = Solution()
print(solution.maxNumberOfFamilies(n, reservedSeats))
