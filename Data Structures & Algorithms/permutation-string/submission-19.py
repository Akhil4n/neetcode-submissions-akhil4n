class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq1 = Counter(s1)
        freq2 = Counter()
        for i in range(len(s1)):
            freq2[s2[i]] += 1

        matches = 0
        for k in freq1:
            if freq1[k] == freq2[k]:
                matches += 1

        if matches == len(freq1):
            return True

        for r in range(len(s1), len(s2)):
            lVal, rVal = s2[r - len(s1)], s2[r]

            freq2[rVal] += 1
            if rVal in freq1:
                if freq2[rVal] == freq1[rVal]:
                    matches += 1
                elif freq2[rVal] == freq1[rVal] + 1:
                    matches -= 1

            freq2[lVal] -= 1
            if lVal in freq1:
                if freq2[lVal] == freq1[lVal]:
                    matches += 1
                elif freq2[lVal] == freq1[lVal] - 1:
                    matches -= 1
            
            if matches == len(freq1):
                return True

        return False


