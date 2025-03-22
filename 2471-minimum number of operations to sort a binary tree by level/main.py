# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # pre-process
        # bfs
        from collections import deque
        bfs = deque()
        bfs.append(root)

        ans = 0
        while bfs:
            size = len(bfs)
            from heapq import heapify, heappush, heappop
            heap = list()
            heapify(heap)
            from collections import defaultdict
            nodes = defaultdict(int)
            vals = list()
            for x in range(size):
                node = bfs.popleft()
                heappush(heap, node.val)
                nodes[node.val] = x
                vals.append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)

            # process
            idx = 0
            while heap:
                val = heappop(heap)
                if nodes[val] != idx:
                    swapped = vals[idx]
                    vals[nodes[val]] = swapped
                    vals[idx] = val
                    nodes[swapped] = nodes[val]
                    nodes[val] = idx
                    ans += 1
                idx += 1
        return ans


"""
node = TreeNode(1)
node2 = TreeNode(4)
node3 = TreeNode(3)
node4 = TreeNode(7)
node5 = TreeNode(6)
node6 = TreeNode(8)
node7 = TreeNode(5)
node8 = TreeNode(9)
node9 = TreeNode(10)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node6.left = node8
node7.left = node9
"""

"""
node = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)
node4 = TreeNode(7)
node5 = TreeNode(6)
node6 = TreeNode(5)
node7 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
"""

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
"""

node = TreeNode(49)
node2 = TreeNode(45)
node3 = TreeNode(1)
node4 = TreeNode(20)
node5 = TreeNode(46)
node6 = TreeNode(15)
node7 = TreeNode(39)
node8 = TreeNode(27)
node9 = TreeNode(25)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node6.left = node9

solution = Solution()
print(solution.minimumOperations(node))
