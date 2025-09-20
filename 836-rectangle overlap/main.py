class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # pre-process
        # helper function
        # get center point
        def center(rec):
            cx = rec[0] + ((rec[2] - rec[0]) * 1.0) / 2
            cy = rec[1] + ((rec[3] - rec[1]) * 1.0) / 2
            return cx, cy

        # get wide and height
        def wh(rec):
            w = rec[2] - rec[0]
            h = rec[3] - rec[1]
            return w, h

        cx1, cy1 = center(rec1)
        cx2, cy2 = center(rec2)

        w1, h1 = wh(rec1)
        w2, h2 = wh(rec2)

        # process
        if abs(cx1 - cx2) < ((w1 + w2) * 1.0) / 2:
            if abs(cy1 - cy2) < ((h1 + h2) * 1.0) / 2:
                return True
        return False


rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]

rec1 = [0,0,1,1]
rec2 = [2,2,3,3]

rec1 = [7,8,13,15]
rec2 = [10,8,12,20]

solution = Solution()
print(solution.isRectangleOverlap(rec1, rec2))
