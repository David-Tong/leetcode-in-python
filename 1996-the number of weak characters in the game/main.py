class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        stack = []
        for _, _defence in properties:
            while stack and stack[-1] < _defence:
                ans += 1
                stack.pop()
            stack.append(_defence)
        return ans


properties = [[3, 2], [5, 3], [5, 5], [6, 1], [7, 2], [8, 3]]

solution = Solution()
print(solution.numberOfWeakCharacters(properties))
