class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        mheap = []
        for char, freq in count.items():
            heapq.heappush(mheap, (freq * -1, char))
        prev = None
        res = []
        while mheap or prev:
            if prev and not mheap:
                return ""
            cnt, char = heapq.heappop(mheap)
            res.append(char)
            cnt += 1
            
            if prev:
                heapq.heappush(mheap, prev)
                prev = None
            
            if cnt != 0:
                prev = (cnt, char)

        return "".join(res)
