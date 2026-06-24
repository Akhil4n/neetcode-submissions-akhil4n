class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagramMap = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                ind = ord(c) - ord('a')
                key[ind] += 1
            anagramMap[tuple(key)].append(s)

        return [ v for v in anagramMap.values() ]