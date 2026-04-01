class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        edges.sort()

        for i in range(len(edges)):
            v1, v2 = edges[i]
            if v1 in seen and v2 in seen:
                return False
            if i > 0 and v1 not in seen and v2 not in seen:
                return False
            if v1 == v2:
                return False
            seen.add(v1)
            seen.add(v2)

        return True