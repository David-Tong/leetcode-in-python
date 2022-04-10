class Solution:
    def isValidSerialization(self, preorder):
        if preorder == '#':
            return True

        class ValidateStack:
            def __init__(self):
                self.stack = []

            def add(self, item):
                self.stack.append(item)
                #print(self.stack)
                if len(self.stack) >= 3:
                    if self.stack[-1] == self.stack[-2] == '#' and self.stack[-3].isdigit():
                        for i in range(3):
                            self.stack.pop()
                        self.add('#')
                #print(self.stack)

            def validate(self):
                if len(self.stack) == 1 and self.stack[0] == '#':
                    return True
                else:
                    return False

        orders = preorder.split(',')
        stack = ValidateStack()
        for order in orders:
            stack.add(order)

        return stack.validate()


preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
preorder = "1,#"
preorder = "9,#,#,1"
preorder = "9,#,92,#,#"

sol = Solution()
print(sol.isValidSerialization(preorder))


