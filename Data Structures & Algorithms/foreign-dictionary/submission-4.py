class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = 0
                adjList[c] = []

        for i in range(1, len(words)):
            prev, curr = words[i - 1], words[i]
            p1 = p2 = 0
            while p1 < len(prev) and p2 < len(curr) and prev[p1] == curr[p2]:
                p1 += 1
                p2 += 1
            if p2 == len(curr) and len(curr) < len(prev):
                return ""
            if p1 < len(prev) and p2 < len(curr):
                indegree[curr[p2]] += 1
                adjList[prev[p1]].append(curr[p2])
        
        q = deque()
        res = []
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in adjList[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return "".join(res) if len(res) == len(indegree) else ""