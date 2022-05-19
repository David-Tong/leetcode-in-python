class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        preorder = preorder.split(",")
        for node in preorder:
            # (node, False) - this is not a leaf node
            if node == "#":
                stack.append([node, True])
            else:
                stack.append([node, False])

            # validate
            while len(stack) >= 2 and stack[-1][1] and stack[-2][1]:
                stack.pop()
                stack.pop()
                if stack:
                    stack[-1][1] = True
                else:
                    return False

        if len(stack) == 1 and stack[0][1]:
            return True
        else:
            return False


preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
preorder = "1,#"
preorder = "9,#,#,1"
preorder = "9,3,4,#,#,#,#"

solution = Solution()
print(solution.isValidSerialization(preorder))
