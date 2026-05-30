class AVLNode:
    def __init__(self, key):
        self.key = key              # obstacle position
        self.left = None
        self.right = None
        self.height = 1

        # augmented info for subtree
        self.min_key = key          # minimum key in subtree
        self.max_key = key          # maximum key in subtree
        self.slot = 0               # maximum gap between consecutive obstacles in subtree


class AVLTree:
    def _height(self, node):
        return node.height if node else 0

    def _update(self, node):
        if not node:
            return None

        # update height
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # update min_key and max_key
        node.min_key = node.key
        node.max_key = node.key
        if node.left:
            node.min_key = min(node.min_key, node.left.min_key)
            node.max_key = max(node.max_key, node.left.max_key)
        if node.right:
            node.min_key = min(node.min_key, node.right.min_key)
            node.max_key = max(node.max_key, node.right.max_key)

        # update slot (max gap between consecutive obstacles in subtree)
        slot = 0
        if node.left:
            slot = max(slot, node.left.slot)
            slot = max(slot, node.key - node.left.max_key)
        if node.right:
            slot = max(slot, node.right.slot)
            slot = max(slot, node.right.min_key - node.key)
        node.slot = slot

        return node

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

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
        bf = self._balance_factor(node)

        if bf > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if bf < -1:
            if self._balance_factor(node.right) > 0:
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
        else:
            return node  # no duplicates
        return self._rebalance(node)

    # query prefix [0, x]: aggregate min_key, max_key, slot among obstacles <= x
    def _query_prefix(self, node, x):
        # returns (min_key, max_key, slot, exists)
        if not node:
            return (None, None, 0, False)

        if node.key > x:
            return self._query_prefix(node.left, x)

        # node.key <= x: include left subtree fully, node itself, and prefix of right subtree
        # left subtree (all <= node.key <= x)
        if node.left:
            lmin, lmax, lslot, lexist = (node.left.min_key,
                                         node.left.max_key,
                                         node.left.slot,
                                         True)
        else:
            lmin = lmax = None
            lslot = 0
            lexist = False

        # right subtree prefix
        rmin, rmax, rslot, rexist = self._query_prefix(node.right, x)

        # combine
        exists = True
        # min_key
        if lexist:
            min_key = lmin
        else:
            min_key = node.key

        # max_key
        if rexist:
            max_key = rmax
        else:
            max_key = node.key

        # slot
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
        tree = AVLTree()
        root = None
        results = []

        for query in queries:
            if query[0] == 1:
                x = query[1]
                root = tree.insert(root, x)
            else:
                _, x, sz = query
                if not root:
                    # no obstacles at all
                    results.append(x >= sz)
                    continue

                min_key, max_key, slot, exists = tree._query_prefix(root, x)

                if not exists:
                    # no obstacles <= x
                    max_free = x  # [0, x]
                else:
                    # gaps: [0, first_obstacle], between obstacles (slot), [last_obstacle, x]
                    first_gap = min_key - 0
                    last_gap = x - max_key
                    max_free = max(first_gap, slot, last_gap)

                results.append(max_free >= sz)

        return results


queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

import random
queries = list()
obstacles = set()
for _ in range(10 ** 4):
    type = random.randint(1, 2)
    obstacle = random.randint(1, 3 * 10 ** 4)
    while obstacle in obstacles:
        obstacle = random.randint(1, 3 * 10 ** 4)
        if obstacle not in obstacles:
            obstacles.add(obstacle)
    if type == 1:
        queries.append([type, obstacle])
    elif type == 2:
        sz = obstacle - random.randint(1, 200)
        queries.append([type, obstacle, sz])
print(queries)

solution = Solution()
print(solution.getResults(queries))
