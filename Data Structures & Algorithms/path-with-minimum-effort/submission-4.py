class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        seen = set()
        heap = [(0, 0, 0)]
        dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        rows, cols = len(heights), len(heights[0])

        while heap:
            wgt, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return wgt
            if (r, c) in seen:
                continue
            seen.add((r, c))
            for x, y in dirs:
                n_r, n_c = r + y, c + x
                if min(n_r, n_c) < 0 or n_r >= rows or n_c >= cols or (n_r, n_c) in seen:
                    continue
                heapq.heappush(heap, (max(wgt, abs(heights[r][c] - heights[n_r][n_c])), n_r, n_c))
        
