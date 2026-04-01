class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i] or
                (r, c) in seen
            ):
                return False

            seen.add((r, c))

            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )

            seen.remove((r, c))
            return found

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False
