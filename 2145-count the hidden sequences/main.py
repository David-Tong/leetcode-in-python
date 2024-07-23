class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # pre-process
        mini = float("inf")
        maxi = float("-inf")

        delta = 0
        for difference in differences:
            delta += difference
            mini = min(mini, delta)
            maxi = max(maxi, delta)

        # process
        left = lower - min(0, mini)
        right = upper - max(0, maxi)

        ans = right - left + 1 if left <= right else 0
        return ans


differences = [1,-3,4]
lower = 1
upper = 6

differences = [3,-4,5,1,-2]
lower = -4
upper = 5

differences = [4,-7,2]
lower = 3
upper = 6

differences = [-40]
lower = -46
upper = 53

differences = [30]
lower = -55
upper = 66

solution = Solution()
print(solution.numberOfArrays(differences, lower, upper))
