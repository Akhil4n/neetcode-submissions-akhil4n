class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):
            par_a, par_b = find(a), find(b)
            if rank[par_a] >= rank[par_b]:
                parent[par_b] = par_a
                rank[par_a] += 1
            else:
                parent[par_a] = par_b
                rank[par_b] += 1
        
        res = None
        for i in range(len(edges)):
            a, b = edges[i]
            if find(a) == find(b):
                res = [a, b]
            union(a, b)

        return res
