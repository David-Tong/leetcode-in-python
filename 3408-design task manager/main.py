class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        from collections import defaultdict
        self.dicts = defaultdict(int)
        self.deleted = defaultdict(list)

        from heapq import heapify
        self.heap = list()
        heapify(self.heap)

        for task in tasks:
            self.add(*task)

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        if taskId in self.dicts:
            version = self.dicts[taskId][0]
            self.deleted[taskId].append(version)
            version += 1
        else:
            version = 1

        from heapq import heappush
        heappush(self.heap, (-1 * priority, -1 * taskId, version, userId))
        self.dicts[taskId] = (version, userId)

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        _, userId = self.dicts[taskId]
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        version, userId = self.dicts[taskId]
        self.deleted[taskId].append(version)

    def execTop(self):
        """
        :rtype: int
        """
        from heapq import heappop

        res = -1
        while self.heap:
            _, taskId, version, userId = heappop(self.heap)
            taskId = -1 * taskId
            if version not in self.deleted[taskId]:
                res = userId
                self.deleted[taskId].append(version)
                break
        return res


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

tasks = [[1, 101, 10], [2, 102, 20], [3, 103, 15]]
tm = TaskManager(tasks)
task = [4, 104, 5]
tm.add(*task)
tm.edit(*[102, 8])
print(tm.execTop())
tm.rmv(101)
task = [5, 105, 15]
tm.add(*task)
print(tm.execTop())

"""
tasks = [[10,26,25]]
tm = TaskManager(tasks)
tm.rmv(26)
print(tm.execTop())
"""

"""
tasks = [[9,0,6],[2,26,9]]
tm = TaskManager(tasks)
tm.rmv(26)
tm.edit(*[0, 49])
tm.rmv(0)
task = [7,0,1]
tm.add(*task)
tm.edit(*[0, 50])
task = [3,2,37]
tm.add(*task)
tm.rmv(2)
print(tm.execTop())
task = [3,2,3]
tm.add(*task)
tm.rmv(2)
print(tm.execTop())
print(tm.execTop())
task = [5,13,14]
tm.add(*task)
print(tm.execTop())
"""

"""
tasks = [[1,101,8],[2,102,20],[3,103,5]]
tm = TaskManager(tasks)
task = [4,104,5]
tm.add(*task)
tm.edit(*[102, 9])
print(tm.execTop())
tm.rmv(101)
task = [50,101,8]
tm.add(*task)
print(tm.execTop())
"""