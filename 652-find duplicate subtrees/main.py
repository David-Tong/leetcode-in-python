class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        import sys
        sys.setrecursionlimit(5003)

        from collections import defaultdict
        structs = defaultdict(bool)

        ans = list()

        def doFind(node):
            struct = ""

            if not node.left and not node.right:
                pass
            else:
                if node.left:
                    struct += str(node.left.val) + "L" + doFind(node.left)
                else:
                    struct += "NA" + "L"
                if node.right:
                    struct += str(node.right.val) + "R" + doFind(node.right)
                else:
                    struct += "NA" + "R"

            key = str(node.val) + "T" + struct
            if key in structs:
                structs[key] += 1
                if structs[key] == 2:
                    ans.append(node)
            else:
                structs[key] = 1
            return struct

        doFind(root)
        return ans


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(2)
node6 = TreeNode(4)
node7 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node5.left = node7

nodes = [TreeNode(0) for _ in range(997)]
for idx, node in enumerate(nodes):
    if idx + 1 < len(nodes):
        node.right = nodes[idx + 1]
node = nodes[0]

node = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(11)
node4 = TreeNode(11)
node5 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
"""

node = TreeNode(10)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(0)
node5 = TreeNode(2)
node6 = TreeNode(3)
node7 = TreeNode(0)

node.left = node2
node.right = node5
node2.left = node3
node3.right = node4
node5.left = node6
node.right = node7

solution = Solution()
print(solution.findDuplicateSubtrees(node))
