# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        from collections import defaultdict
        self.ans = 0

        def doCount(node):
            if node.val == 78:
                pass
            if not node.left and not node.right:
                dists = defaultdict(int)
                dists[1] = 1
                return dists
            else:
                if node.left:
                    left_dists = doCount(node.left)
                else:
                    left_dists = None
                if node.right:
                    right_dists = doCount(node.right)
                else:
                    right_dists = None

                # calculate
                if left_dists and right_dists:
                    for left_dist in left_dists:
                        for right_dist in right_dists:
                            if left_dist + right_dist <= distance:
                                self.ans += left_dists[left_dist] * right_dists[right_dist]

                # merge
                dists = defaultdict(int)
                if left_dists:
                    for left_dist in left_dists:
                        dists[left_dist + 1] += left_dists[left_dist]
                if right_dists:
                    for right_dist in right_dists:
                        dists[right_dist + 1] += right_dists[right_dist]
                return dists

        doCount(root)
        return self.ans


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.left = node2
node.right = node3
node2.right = node4

distance = 3
"""

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

distance = 3
"""

"""
node = TreeNode(7)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(6)
node5 = TreeNode(5)
node6 = TreeNode(3)
node7 = TreeNode(2)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node6.right = node7

distance = 3
"""

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9
node7.right = node10

distance = 3
"""

node = TreeNode(78)
node2 = TreeNode(15)
node3 = TreeNode(81)
node4 = TreeNode(73)
node5 = TreeNode(98)
node6 = TreeNode(36)
node7 = TreeNode(30)
node8 = TreeNode(63)
node9 = TreeNode(32)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node4.left = node7
node5.left = node8
node5.right = node9

distance = 6

solution = Solution()
print(solution.countPairs(node, distance))