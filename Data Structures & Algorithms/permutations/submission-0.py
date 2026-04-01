class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = [-10] * len(nums)
        seen = set(nums)
        def dfs(i, seen):
            if i >= len(cur):
                res.append(cur.copy())
                return
            for s in seen:
                cur_seen = seen.copy()
                cur[i] = s
                cur_seen.remove(s)
                dfs(i+1, cur_seen)

        dfs(0, seen)
        print(res)
        return res