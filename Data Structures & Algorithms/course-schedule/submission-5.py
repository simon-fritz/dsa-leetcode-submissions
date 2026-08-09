class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []:
                return True
            visiting.add(course)
            for precourse in preMap[course]:
                if not dfs(precourse):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not(dfs(c)):
                return False
        return True



                
