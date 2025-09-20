class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        # process
        stack = list()
        ans = 0
        for direction in directions:
            if not stack:
                stack.append(direction)
            else:
                if direction == "L":
                    if stack[-1] == "R":
                        stack[-1] = "S"
                        stack.append("S")
                        ans += 2
                    elif stack[-1] == "S":
                        stack.append("S")
                        ans += 1
                elif direction == "S":
                    if stack[-1] == "R":
                        stack[-1] = "S"
                        ans += 1
                    stack.append(direction)
                else:
                    stack.append(direction)
        # print(ans)
        # print(stack)

        # post-process
        count = 0
        for direction in stack:
            if direction == "R":
                count += 1
            else:
                ans += count
                count = 0

        return ans


directions = "RLRSLL"
directions = "LLRR"
directions = "LRLLLSSLRRRLS"
directions = "LSSSLLSSSSLRRSLLLSLSLRRLLLLLRSSRSRRSLLLSSS"
directions = "LSSSLLSSSS"

solution = Solution()
print(solution.countCollisions(directions))
