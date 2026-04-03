class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for pair in prerequisites:
            crs, pre = pair[0], pair[1]
            adj[pre].append(crs)

        seen = set()
        stackSet = set()
        
        def dfs(i):
            seen = set()
            seen.add(i)
            stackSet.add(i)
            for crs in adj[i]:
                if crs in stackSet:
                    return False
                if not dfs(crs):
                    return False
            stackSet.remove(i)
            return True


        for i in range(numCourses):
            if i not in seen and not dfs(i):
                return False

        return True