# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        importances = defaultdict(int)
        
        for employee in employees:
            graph[employee.id].extend(employee.subordinates)
            importances[employee.id] = employee.importance
        
        total = importances[id]
        def dfs(id):
            nonlocal total
            
            for neighbour in graph[id]:
                total += importances[neighbour]
                dfs(neighbour)
        
        dfs(id)
        return total