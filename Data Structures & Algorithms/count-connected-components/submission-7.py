class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(i):
            if parent[i] != i:
                return find(parent[i])
            else:
                return i

        def union(a, b):
            a_par, b_par = find(a), find(b)
            if a_par == b_par:
                return False
            if rank[a_par] > rank[b_par]:
                parent[b_par] = a_par
                rank[a_par] += 1
            else:
                parent[a_par] = b_par
                rank[b_par] += 1
            return True
        
        res = n
        for e in edges:
            if union(e[0], e[1]):
                res -= 1
        
        return res
        
