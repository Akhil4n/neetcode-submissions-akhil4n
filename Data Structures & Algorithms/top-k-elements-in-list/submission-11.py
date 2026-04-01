class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for _ in range(len(nums) + 1)]
        freqMap = Counter(nums)

        for key, value in freqMap.items():
            freq[value].append(key)

        for i in range(len(freq) - 1, 0, -1):
            curr = freq[i]
            for c in curr:
                res.append(c)
            if len(res) == k:
                break
        
        return res
