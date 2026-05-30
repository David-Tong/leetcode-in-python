class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

        # subtree info
        self.min_key = key
        self.max_key = key
        # max gap between consecutive obstacles *inside this subtree only*
        self.slot = 0


class AVLTree:
    def _height(self, node):
        return node.height if node else 0

    def _update(self, node):
        if not node:
            return None

        # update height
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # update min/max in subtree
        node.min_key = node.key
        node.max_key = node.key
        if node.left:
            node.min_key = node.left.min_key
            node.max_key = max(node.max_key, node.left.max_key)
        if node.right:
            node.max_key = node.right.max_key
            node.min_key = min(node.min_key, node.right.min_key)

        # update slot:
        # only internal gaps between obstacles in this subtree,
        # do NOT include [0, first_obstacle] or [+inf, last_obstacle]
        slot = 0
        if node.left:
            # gaps fully inside left subtree
            slot = max(slot, node.left.slot)
            # gap between left.max_key and node.key
            slot = max(slot, node.key - node.left.max_key)
        if node.right:
            # gaps fully inside right subtree
            slot = max(slot, node.right.slot)
            # gap between node.key and right.min_key
            slot = max(slot, node.right.min_key - node.key)

        node.slot = slot
        return node

    def _bf(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update(y)
        self._update(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update(x)
        self._update(y)
        return y

    def _rebalance(self, node):
        self._update(node)
        bf = self._bf(node)

        if bf > 1:
            if self._bf(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if bf < -1:
            if self._bf(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        # no duplicates
        return self._rebalance(node)

    # prefix query: obstacles with key <= x
    # returns (min_key, max_key, slot, exists)
    def query_prefix(self, node, x):
        if not node:
            return (None, None, 0, False)

        if node.key > x:
            return self.query_prefix(node.left, x)

        # node.key <= x
        # left subtree is fully included
        if node.left:
            lmin, lmax, lslot, lexist = (
                node.left.min_key,
                node.left.max_key,
                node.left.slot,
                True
            )
        else:
            lmin = lmax = None
            lslot = 0
            lexist = False

        # right subtree: only prefix <= x
        rmin, rmax, rslot, rexist = self.query_prefix(node.right, x)

        exists = True

        # min_key in prefix
        if lexist:
            min_key = lmin
        else:
            min_key = node.key

        # max_key in prefix
        if rexist:
            max_key = rmax
        else:
            max_key = node.key

        # slot inside prefix: combine left, node, right
        slot = max(lslot, rslot)
        if lexist:
            slot = max(slot, node.key - lmax)
        if rexist:
            slot = max(slot, rmin - node.key)

        return (min_key, max_key, slot, exists)


class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # pre-process
        tree = AVLTree()
        root = None
        ans = []

        # process
        for query in queries:
            if query[0] == 1:
                # type 1: add obstacle at x
                root = tree.insert(root, query[1])
            else:
                # type 2: can we place block of size sz in [0, x]?
                _, x, sz = query
                if not root:
                    ans.append(x >= sz)
                    continue

                mn, mx, slot, exists = tree.query_prefix(root, x)

                if not exists:
                    # no obstacles <= x
                    ans.append(x >= sz)
                    continue

                # free segments in [0, x]:
                # [0, mn], internal gaps (slot), [mx, x]
                first_gap = mn - 0
                last_gap = x - mx
                best = max(first_gap, slot, last_gap)
                ans.append(best >= sz)

        return ans


# quick check with your examples
queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

print(Solution().getResults(queries))
