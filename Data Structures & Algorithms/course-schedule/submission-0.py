class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for p in prerequisites:
            k, v = p[0], p[1]
            preMap[k].append(v)
        seen = set()
        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
            seen.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            preMap[crs] = []
            return True
        for k in range(numCourses):
            if not dfs(k):
                return False
        return True
