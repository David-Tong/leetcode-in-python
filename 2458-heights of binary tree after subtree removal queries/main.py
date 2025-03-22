# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        dicts = defaultdict(dict)

        def dfs(node, level):
            dicts[node.val]["level"] = level
            dicts[node.val]["value"] = node.val
            height = 0
            if node.left:
                height = max(height, dfs(node.left, level + 1))
            if node.right:
                height = max(height, dfs(node.right, level + 1))
            dicts[node.val]["height"] = height

            return height + 1

        # pre-process
        # build level and height map
        height = dfs(root, 0) - 1
        # print(height)

        # build level lookup table
        levels = defaultdict(list)
        for value in dicts:
            level = dicts[value]["level"]
            levels[level].append((dicts[value]["height"], value))
        for level in levels:
            levels[level] = sorted(levels[level], key=lambda x: -x[0])
        # print(levels)

        # process
        ans = list()
        for query in queries:
            level = dicts[query]["level"]
            # query the node with the largest height at the level
            if query == levels[level][0][1]:
                if len(levels[level]) == 1:
                    ans.append(level - 1)
                else:
                    ans.append(level + levels[level][1][0])
            # remove node will not change tree height
            else:
                ans.append(height)

        return ans


"""
node = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(2)
node5 = TreeNode(6)
node6 = TreeNode(5)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node6.right = node7

queries = [4]
"""

node = TreeNode(5)
node2 = TreeNode(8)
node3 = TreeNode(9)
node4 = TreeNode(2)
node5 = TreeNode(1)
node6 = TreeNode(3)
node7 = TreeNode(7)
node8 = TreeNode(4)
node9 = TreeNode(6)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9

queries = [3,2,4,8]

solution = Solution()
print(solution.treeQueries(node, queries))
