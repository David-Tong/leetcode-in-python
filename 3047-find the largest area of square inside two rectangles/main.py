class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(bottomLeft)

        # helper function
        def getInsideSquare(x, y):
            x1_x, y1_x, x2_x, y2_x = bottomLeft[x][0], bottomLeft[x][1], topRight[x][0], topRight[x][1]
            x1_y, y1_y, x2_y, y2_y = bottomLeft[y][0], bottomLeft[y][1], topRight[y][0], topRight[y][1]

            # Find the coordinates of the intersection rectangle
            # The left edge of the intersection is the rightmost of the two left edges
            overlap_x1 = max(x1_x, x1_y)
            # The bottom edge of the intersection is the topmost of the two bottom edges
            overlap_y1 = max(y1_x, y1_y)
            # The right edge of the intersection is the leftmost of the two right edges
            overlap_x2 = min(x2_x, x2_y)
            # The top edge of the intersection is the bottommost of the two top edges
            overlap_y2 = min(y2_x, y2_y)

            # Calculate width and height of the overlap
            overlap_width = overlap_x2 - overlap_x1
            overlap_height = overlap_y2 - overlap_y1

            # If width or height is negative, they don't overlap
            if overlap_width <= 0 or overlap_height <= 0:
                return 0
            else:
                return min(overlap_width, overlap_height) ** 2

        # process
        ans = 0
        for x in range(L):
            for y in range(x + 1, L):
                # print(x, y ,getInsideSquare(x, y))
                ans = max(ans, getInsideSquare(x, y))
        return ans


bottomLeft = [[1,1],[2,2],[3,1]]
topRight = [[3,3],[4,4],[6,6]]

bottomLeft = [[1,1],[1,3],[1,5]]
topRight = [[5,5],[5,7],[5,9]]

bottomLeft = [[1,1],[2,2],[1,2]]
topRight = [[3,3],[4,4],[3,4]]

bottomLeft = [[1,1],[3,3],[3,1]]
topRight = [[2,2],[4,4],[4,2]]

bottomLeft = [[1,2],[1,2]]
topRight = [[4,5],[2,3]]

bottomLeft = [[2,2],[1,3]]
topRight = [[3,4],[5,5]]

solution = Solution()
print(solution.largestSquareArea(bottomLeft, topRight))
