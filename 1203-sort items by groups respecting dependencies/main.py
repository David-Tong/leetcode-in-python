class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        def getName(idx):
            if group[idx] >= 0:
                return "g" + str(group[idx])
            else:
                return "i" + str(idx)

        # pre-process
        from collections import defaultdict
        before_group_items = defaultdict(set)
        group_items_dependents = defaultdict(set)
        for idx, items in enumerate(beforeItems):
            if getName(idx) not in before_group_items:
                before_group_items[getName(idx)] = set()
            for item in items:
                if getName(item) != getName(idx):
                    before_group_items[getName(idx)].add(getName(item))
                    group_items_dependents[getName(item)].add(getName(idx))
        #print(before_group_items)
        #print(group_items_dependents)

        # topological sort
        group_items_ingree = defaultdict(int)
        for key in before_group_items:
            group_items_ingree[key] += len(before_group_items[key])
        #print(before_group_items.keys())
        #print(group_items_ingree)

        from collections import deque
        queue = deque()
        for key in group_items_ingree:
            if group_items_ingree[key] == 0:
                queue.append(key)

        group_items_order = list()
        while queue:
            curr = queue.popleft()
            group_items_order.append(curr)
            if curr in group_items_dependents:
                for depend in group_items_dependents[curr]:
                    group_items_ingree[depend] -= 1
                    if group_items_ingree[depend] == 0:
                        queue.append(depend)

        if len(group_items_order) != len(group_items_ingree):
            return list()

        # topological sort for item
        item_in_degree = [0] * n
        item_dependents = defaultdict(list)
        for idx, before_items in enumerate(beforeItems):
            for before_item in before_items:
                item_dependents[before_item].append(idx)
            item_in_degree[idx] = len(before_items)

        queue = deque()
        for idx, in_degree in enumerate(item_in_degree):
            if in_degree == 0:
                queue.append(idx)

        item_order = list()
        while queue:
            node = queue.popleft()
            item_order.append(node)
            if node in item_dependents:
                for dependent in item_dependents[node]:
                    item_in_degree[dependent] -= 1
                    if item_in_degree[dependent] == 0:
                        queue.append(dependent)
        #print(item_order)

        if len(item_order) != len(item_in_degree):
            return list()

        item_order_by_group = defaultdict(list)
        for item in item_order:
            if group[item] >= 0:
                item_order_by_group[getName(item)].append(item)
        #print(item_order_by_group)

        ans = list()
        for item in group_items_order:
            if item[0] == "i":
                ans.append(int(item[1:]))
            elif item[0] == "g":
                ans.extend(item_order_by_group[item])
        return ans


n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
beforeItems = [[],[6],[3,5],[6],[3,6],[],[5],[]]

solution = Solution()
print(solution.sortItems(n, m, group, beforeItems))
