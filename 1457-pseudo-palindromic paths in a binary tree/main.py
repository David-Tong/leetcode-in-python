class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def leftMost(node, stack, paths):
            while node:
                stack.append(node)
                paths[node.val] = 1 - paths[node.val]
                node = node.left

        stack = list()
        visited = set()
        from collections import defaultdict
        paths = defaultdict(int)
        leftMost(root, stack, paths)

        ans = 0
        while stack:
            if stack[-1] in visited:
                if not stack[-1].left and not stack[-1].right:
                    total = sum(paths.values())
                    if total == 0 or total == 1:
                        ans += 1
                node = stack.pop()
                paths[node.val] = 1 - paths[node.val]
            else:
                visited.add(stack[-1])
                node = stack[-1].right
                leftMost(node, stack, paths)
        return ans


"""
node = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(1)
node6 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
"""

node = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(1)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node5.right = node6

solution = Solution()
print(solution.pseudoPalindromicPaths(node))
