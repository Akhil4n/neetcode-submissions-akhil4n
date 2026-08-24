class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        candidates.sort()
        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            if i == len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i+1, total + candidates[i])
            curr.pop()
            n = i
            while n + 1 < len(candidates) and candidates[n] == candidates[n+1]:
                n += 1
            dfs(n+1, total)
        dfs(0, 0)
        return res