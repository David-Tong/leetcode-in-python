class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from bisect import bisect_left
        def insert(ordered, height):
            height = -1 * height
            idx = bisect_left(ordered, height)
            ordered = ordered[:idx] + [height] + ordered[idx:]
            return ordered

        def delete(ordered, height):
            height = -1 * height
            idx = bisect_left(ordered, height)
            ordered = ordered[:idx] + ordered[idx+1:]
            return ordered

        def getMaxHeight(ordered):
            return -1 * ordered[0] if len(ordered) > 0 else 0

        from functools import cmp_to_key
        def compare(point, point2):
            if point[0] < point2[0]:
                return -1
            elif point[0] > point2[0]:
                return 1
            else:
                if point[2] < point2[2]:
                    return 1
                elif point[2] > point2[2]:
                    return -1
                else:
                    if point[2] == 1:
                        if point[1] < point2[1]:
                            return 1
                        elif point[1] > point2[1]:
                            return -1
                    elif point[2] == -1:
                        if point[1] < point2[1]:
                            return -1
                        elif point[1] > point2[1]:
                            return 1
            return 0

        points = []
        for building in buildings:
            points.append((building[0], building[2], 1))
            points.append((building[1], building[2], -1))
        points = sorted(points, key=cmp_to_key(compare))
        ordered = []
        height = 0
        skylines = []
        for point in points:
            if point[2] == 1:
                ordered = insert(ordered, point[1])
            elif point[2] == -1:
                ordered = delete(ordered, point[1])
            new_height = getMaxHeight(ordered)
            if height != new_height:
                height = new_height
                skylines.append((point[0], new_height))
        return skylines


buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
buildings = [[0,2,3],[2,5,3]]
buildings = [[1,4,1],[2,4,2],[3,4,3]]
buildings = [[1,2,1],[1,2,2],[1,2,3]]

solution = Solution()
print(solution.getSkyline(buildings))
