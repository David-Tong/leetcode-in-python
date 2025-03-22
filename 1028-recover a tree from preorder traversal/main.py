# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        # parse traversal
        L = len(traversal)
        idx = 0
        isNum = True
        start, end = 0, 0
        level = 0
        while idx < L:
            if traversal[idx] == "-":
                if isNum:
                    isNum = False
                    end = idx
                    if level > 0:
                        dicts[level].append((start, end))
                    level = 0
                level += 1
            else:
                if not isNum:
                    isNum = True
                    start = idx
            idx += 1
        end = idx
        if level > 0:
            dicts[level].append((start, end))

        print(dicts)

        # process
        # regression function
        def build(node, start, end, level):
            idxes = dicts[level]
            child_idxes = list()
            for idx_start, idx_end in idxes:
                if start < idx_start < end:
                    child_idxes.append((idx_start, idx_end))
            # only left child
            if len(child_idxes) == 1:
                left_child = TreeNode(int(traversal[child_idxes[0][0]:child_idxes[0][1]]))
                node.left = left_child
                build(left_child, child_idxes[0][0], end, level + 1)
            # has both left and right children
            elif len(child_idxes) == 2:
                left_child = TreeNode(int(traversal[child_idxes[0][0]:child_idxes[0][1]]))
                node.left = left_child
                build(left_child, child_idxes[0][0], child_idxes[1][0], level + 1)
                right_child = TreeNode(int(traversal[child_idxes[1][0]:child_idxes[1][1]]))
                node.right = right_child
                build(right_child, child_idxes[1][0], end, level + 1)

        node = TreeNode(int(traversal.split("-")[0]))
        build(node, 0, L, 1)
        return node


traversal = "1-2--3--4-5--6--7"
traversal = "1-2--3---4-5--6---7"
traversal = "1-401--349---90--88"
traversal = "10-7--8"

solution = Solution()
node = solution.recoverFromPreorder(traversal)

node
