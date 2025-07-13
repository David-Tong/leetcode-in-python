class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        # process
        ans = 0
        for operation in operations:
            if operation in ["++X", "X++"]:
                ans += 1
            elif operation in ["--X", "X--"]:
                ans -= 1
            else:
                raise ValueError
        return ans


operations = ["--X","X++","X++"]
operations = ["++X","++X","X++"]
operations = ["X++","++X","--X","X--"]

solution = Solution()
print(solution.finalValueAfterOperations(operations))
