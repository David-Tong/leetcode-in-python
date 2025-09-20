# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        """
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        """
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(Employee)

        for employee in employees:
            dicts[employee.id] = employee

        # dfs
        def importance(employee):
            res = employee.importance
            for subordinate in employee.subordinates:
                res += importance(dicts[subordinate])
            return res

        employee = dicts[id]
        ans = importance(employee)
        return ans


"""
employee = Employee(1,5,[2,3])
employee2 = Employee(2,3,[])
employee3 = Employee(3,3,[])

employees = [employee, employee2, employee3]
id = 1
"""

employee = Employee(1,2,[5])
employee2 = Employee(5,-3,[])

employees = [employee, employee2]
id =5

solution = Solution()
print(solution.getImportance(employees, id))
