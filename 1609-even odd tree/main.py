# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        bfs = deque()
        bfs.append(root)

        level = 0
        while bfs:
            nums = list()
            for _ in range(len(bfs)):
                node = bfs.popleft()
                nums.append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            # check
            for idx, num in enumerate(nums):
                if level % 2 == 0:
                    if num % 2 == 0:
                        return False
                    if idx > 0:
                        if nums[idx] <= nums[idx - 1]:
                            return False
                else:
                    if num % 2 == 1:
                        return False
                    if idx > 0:
                        if nums[idx] >= nums[idx - 1]:
                            return False
            level += 1
        return True


"""
node = TreeNode(1)
node2 = TreeNode(10)
node3 = TreeNode(4)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(9)
node7 = TreeNode(12)
node8 = TreeNode(8)
node9 = TreeNode(6)
node10 = TreeNode(2)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node5.left = node9
node6.right = node10
"""

"""
node = TreeNode(6)
node2 = TreeNode(4)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(3)
node6 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
"""

node = TreeNode(5)
node2 = TreeNode(9)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(5)
node6 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

solution = Solution()
print(solution.isEvenOddTree(node))
