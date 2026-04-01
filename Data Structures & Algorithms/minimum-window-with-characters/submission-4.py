class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
            
        tmap = Counter(t)
        matches = 0
        res = ""
        smap = {}
        l, r = 0, 0
        while r < len(s):
            curr = s[r]
            smap[curr] = smap.get(curr, 0) + 1
            if smap[curr] == tmap[curr]:
                matches += 1
            while matches == len(tmap):
                lv = s[l]
                smap[lv] -= 1
                if lv in tmap and smap[lv] == tmap[lv] - 1:
                    matches -= 1
                if matches != len(tmap):
                    cr = s[l:r+1]
                    if res == "" or len(cr) < len(res):
                        res = cr
                l += 1
            r += 1
        return res