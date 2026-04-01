class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rsets = defaultdict(set)    
        csets = defaultdict(set)
        ssets = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rsets[i]:
                    return False
                else:
                    rsets[i].add(num)
                if num in csets[j]:
                    return False
                else:
                    csets[j].add(num)
                skey = (i // 3) * 10 + j // 3
                if num in ssets[skey]:
                    return False
                else:
                    ssets[skey].add(num)
        return True