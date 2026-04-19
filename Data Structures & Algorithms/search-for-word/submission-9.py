class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        def dfs(currInd, i, j, seen):
            if currInd >= len(word):
                return True

            if min(i, j) < 0 or i >= rows or j >= cols or (i, j) in seen or board[i][j] != word[currInd]:
                return False

            seen.add((i, j))
            res = dfs(currInd + 1, i + 1, j, seen) or dfs(currInd + 1, i - 1, j, seen) or dfs(currInd + 1, i, j + 1, seen) or dfs(currInd + 1, i, j - 1, seen)
            seen.remove((i, j))

            return res

        for r in range(rows):
            for c in range(cols):
                seen = set()
                res = dfs(0, r, c, seen)
                if res:
                    return True

        return False