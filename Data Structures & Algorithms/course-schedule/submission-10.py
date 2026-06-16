class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        queue = deque()

        for crs, pre in prerequisites:
            preMap[pre].append(crs)
        
        visiting = set()
        def dfs(i):
            if i in visiting:
                return False
            if len(preMap[i]) == 0:
                return True
            
            visiting.add(i)
            for crs in preMap[i]:
                if not dfs(crs):
                    return False
            visiting.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True