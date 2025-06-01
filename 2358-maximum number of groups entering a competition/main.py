from functools import total_ordering


class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        # pre-process
        L = len(grades)

        # process
        group = 1
        total = 0
        ans = -1
        while total <= L:
            total += group
            group += 1
            ans += 1
        return ans


grades = [10,6,12,7,3,5]
grades = [8,8]
grades = [1]
grades = [10,6,12,7,3,5,6]
grades = [10,6,12,7,3,5,6,7,8,9]

solution = Solution()
print(solution.maximumGroups(grades))
