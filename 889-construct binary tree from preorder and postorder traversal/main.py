# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # process
        # recursion function
        def build(preorder, postorder):
            if len(preorder) != len(postorder):
                raise RuntimeError()
            if len(preorder) == 0:
                return None

            num = preorder[0]
            node = TreeNode(num)
            # process left child
            if len(preorder) > 1:
                left_num = preorder[1]
                post_idx = len(postorder) - 1
                while post_idx >= 0:
                    if postorder[post_idx] == left_num:
                        break
                    post_idx -= 1
                left_preorder_end = 1 + post_idx
                left_preorder = preorder[1:left_preorder_end + 1]
                left_postorder = postorder[:post_idx + 1]
                left_child = build(left_preorder, left_postorder)
                node.left = left_child

                # process right child
                right_preorder_start = left_preorder_end + 1
                right_postorder_start = post_idx + 1
                if right_preorder_start < len(postorder):
                    right_preorder = preorder[right_preorder_start:]
                    right_postorder = postorder[right_postorder_start:-1]
                    right_child = build(right_preorder, right_postorder)
                    node.right = right_child

            return node

        node = build(preorder, postorder)
        return node


preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
preorder = [1]
postorder = [1]
preorder = [1,2,3,4]
postorder = [4,3,2,1]

solution = Solution()
node = solution.constructFromPrePost(preorder, postorder)

node
