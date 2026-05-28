class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(i):
            if parent[i] != i:
                return find(parent[i])
            else:
                return i

        res = n
        def union(a, b):
            nonlocal res
            a_par, b_par = find(a), find(b)
            if a_par == b_par:
                return
            res -= 1
            if rank[a_par] > rank[b_par]:
                parent[b_par] = a_par
                rank[a_par] += 1
            else:
                parent[a_par] = b_par
                rank[b_par] += 1
        
        for e in edges:
            union(e[0], e[1])
        
        return res
        
