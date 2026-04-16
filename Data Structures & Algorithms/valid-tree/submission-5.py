class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]
        rank = [0] * n
        pieces = n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            xpar = find(x)
            ypar = find(y)
            if xpar == ypar:
                return False
            if rank[xpar] < rank[ypar]:
                parents[xpar] = ypar
            else:
               parents[ypar] = xpar
            if rank[xpar] == rank[ypar]:
                rank[xpar] += 1
            return True

        for e in edges:
            u, v = e
            if not union(u, v):
                return False
            pieces -= 1
        return pieces == 1