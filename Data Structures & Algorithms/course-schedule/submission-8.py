class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for pre, course in prerequisites:
            pre_map[course].append(pre)

        #cur dfs path
        visiting = set()

        def dfs(c):
            if c in visiting:
                return False
            if pre_map[c] == []:
                return True
            visiting.add(c)
            for p in pre_map[c]:
                if not dfs(p):
                    return False
            visiting.remove(c)
            pre_map[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True