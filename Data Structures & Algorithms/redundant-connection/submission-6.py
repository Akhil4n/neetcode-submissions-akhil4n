class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def find(num):
            if parent[num] != num:
                parent[num] = find(parent[num])
            return parent[num]

        def union(a, b):
            a_par, b_par = find(a), find(b)
            if a_par == b_par:
                return False
            if rank[a_par] >= rank[b_par]:
                parent[b_par] = a_par
                rank[a_par] += 1
            else:
                parent[a_par] = b_par
                rank[b_par] += 1
            return True
        for e in edges:
            if not union(e[0], e[1]):
                return e

