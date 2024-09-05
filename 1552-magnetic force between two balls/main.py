class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        def canPlace(distance, position, m):
            curr = position[0]
            m -= 1
            for pos in position[1:]:
                if pos - curr >= distance:
                    curr = pos
                    m -= 1
                    if m == 0:
                        return True
            return False

        left = 1
        right = 10 ** 9
        position = sorted(position)

        while left + 1 < right:
            middle = (left + right) // 2
            if middle == 5958:
                pass
            if canPlace(middle, position, m):
                left = middle
            else:
                right = middle - 1

        if canPlace(right, position, m):
            return right
        else:
            return left


position = [1,2,3,4,7]
m = 3

position = [5,4,3,2,1,1000000000]
m = 2

position = [7,4,3,2,1]
m = 3

position = [1, 8]
m = 2

position = [1, 8, 9]
m = 3

position = [5999,2816,4264,2051,1731,5565]
m = 2

solution = Solution()
print(solution.maxDistance(position, m))
