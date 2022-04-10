class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if query_row == 0:
            if poured >= 1:
                return 1
            else:
                return poured

        from collections import deque
        bfs = deque()
        bfs.append(poured)
        row = 0
        while row <= query_row:
            length = len(bfs)
            for x in range(0, length + 1):
                if x == 0:
                    curr = max(0, bfs.popleft() - 1)
                    liquid = 0.5 * curr
                    prev = curr
                elif x == length:
                    liquid = 0.5 * prev
                else:
                    curr = max(0, bfs.popleft() - 1)
                    liquid = 0.5 * (prev + curr)
                    prev = curr
                if row == query_row - 1 and x == query_glass:
                    if liquid >= 1:
                        return 1
                    else:
                        return liquid
                bfs.append(liquid)
            row += 1


poured = 1
query_row = 1
query_glass = 1

poured = 2
query_row = 1
query_glass = 1

poured = 6
query_row = 3
query_glass = 1

poured = 100000009
query_row = 33
query_glass = 17

poured = 0
query_row = 0
query_glass = 0

solution = Solution()
print(solution.champagneTower(poured, query_row, query_glass))
