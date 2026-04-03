class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        seen = set()
        adjmap = defaultdict(list)
        for e in edges:
            adjmap[e[0]].append(e[1])
            adjmap[e[1]].append(e[0])

        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            for j in adjmap[i]:
                dfs(j)

        for i in range(n):
            if i not in seen:
                res += 1
                dfs(i)
        
        return res
