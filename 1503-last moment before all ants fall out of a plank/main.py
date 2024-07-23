class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        max_left = 0
        if left:
            max_left = max(left)

        min_right = n
        if right:
            min_right = min(right)

        return max(n - min_right, max_left)


n = 4
left = [4,3]
right = [0,1]

n = 7
left = []
right = [0,1,2,3,4,5,6,7]

n = 7
left = [0,1,2,3,4,5,6,7]
right = []

n = 10
left = []
right = [0]

solution = Solution()
print(solution.getLastMoment(n, left, right))
