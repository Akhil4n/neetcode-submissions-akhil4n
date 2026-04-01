class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        cnt = Counter(nums)
        for key, v in cnt.items():
            freq[v].append(key)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            if k == 0:
                break
            if len(freq[i]) == 0:
                continue
            k -= len(freq[i])
            for j in range(len(freq[i])):
                res.append(freq[i][j])
        return res