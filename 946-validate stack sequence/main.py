class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        N = len(pushed)
        stack = []
        curr = 0
        for item in popped:
            if len(stack) > 0 and stack[-1] == item:
                stack.pop()
            else:
                if curr == N:
                    return False
                for x in range(curr, N):
                    if pushed[x] == item:
                        curr = x + 1
                        break
                    else:
                        stack.append(pushed[x])
        if len(stack) == 0:
            return True
        else:
            return False


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]

pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]

pushed = [1, 2, 3, 4, 5, 6]
popped = [4, 6, 5, 3, 2, 1]

pushed = [1]
popped = [1]

pushed = [1, 2, 3, 4, 5, 6]
popped = [5, 6, 3, 4, 2, 1]

pushed = [1, 2, 3, 4, 5, 6, 7]
popped = [1, 2, 5, 3, 6, 7, 4]

pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]

pushed = [1, 2, 3, 4, 5, 6, 7]
popped = [1, 2, 5, 3, 6, 7, 4]

#pushed = [1, 2, 3, 4, 5]
#popped = [4, 5, 3, 2, 1]

solution = Solution()
print(solution.validateStackSequences(pushed, popped))
