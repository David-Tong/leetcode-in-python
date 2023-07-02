class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        ps = [p1, p2, p3, p4]
        L = len(ps)

        from collections import defaultdict
        distances = defaultdict(int)
        for x in range(L):
            for y in range(x + 1, L):
                distance = (ps[y][0] - ps[x][0]) ** 2 + (ps[y][1] - ps[x][1]) ** 2
                distances[distance] += 1

        # check
        if len(distances) == 2:
            edge, bevle_edge = min(distances), max(distances)
            if bevle_edge == edge * 2:
                return True
        return False


p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]

p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,12]

p1 = [1,0]
p2 = [-1,0]
p3 = [0,1]
p4 = [0,-1]

p1 = [2, 0]
p2 = [-2, 0]
p3 = [0, -1]
p4 = [0, 1]

solution = Solution()
print(solution.validSquare(p1, p2, p3, p4))
