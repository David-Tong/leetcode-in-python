class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = list()
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                pass
            else:
                stack.append(log)
        return len(stack)


logs = ["d1/","d2/","../","d21/","./"]
logs = ["d1/","d2/","./","d3/","../","d31/"]
logs = ["d1/","../","../","../"]
logs = ["./","../","./"]

solution = Solution()
print(solution.minOperations(logs))
