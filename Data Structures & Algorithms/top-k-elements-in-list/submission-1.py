class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq  = [[] for i in range(len(nums) + 1)]
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        res = []
        for n, c in count.items():
            freq[c].append(n)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
        
        
        
        
        
        
        '''fin = []
        i = len(res)
        while i > len(res) - k:
            fin.append(res[i - 1])
            i -= 1
        return fin'''
            
        