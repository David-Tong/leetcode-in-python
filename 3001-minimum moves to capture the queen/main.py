class Solution(object):
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        """
        :type a: int
        :type b: int
        :type c: int
        :type d: int
        :type e: int
        :type f: int
        :rtype: int
        """
        # check one
        # check rook
        if a == e:
            if a == c:
                if b < d < f or f < d < b:
                    pass
                else:
                    return 1
            else:
                return 1

        if b == f:
            if b == d:
                if a < c < e or e < c < a:
                    pass
                else:
                    return 1
            else:
                return 1

        # check bishop
        DIRECTIONS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        for dx, dy in DIRECTIONS:
            x = c
            y = d
            while 0 < x <= 8 and 0 < y <= 8:
                x += dx
                y += dy
                if x == a and y == b:
                    break
                if x == e and y == f:
                    return 1
        # then two
        return 2


a = 1
b = 1
c = 8
d = 8
e = 2
f = 3

a = 5
b = 3
c = 3
d = 4
e = 5
f = 2

a = 4
b = 3
c = 3
d = 4
e = 5
f = 2

a = 4
b = 3
c = 3
d = 4
e = 2
f = 5

a = 1
b = 6
c = 3
d = 3
e = 5
f = 6

a = 8
b = 4
c = 8
d = 8
e = 7
f = 7

a = 5
b = 8
c = 8
d = 8
e = 1
f = 8

solution = Solution()
print(solution.minMovesToCaptureTheQueen(a, b, c, d, e, f))
