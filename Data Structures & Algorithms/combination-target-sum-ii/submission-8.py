class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i == len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()
            n = i
            while n + 1 < len(candidates) and candidates[n] == candidates[n+1]:
                n += 1
            dfs(n+1, curr, total)
        dfs(0, [], 0)
        return res