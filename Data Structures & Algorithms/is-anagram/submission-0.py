class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
           countS, countT = {}, {}
           x = sorted(s)
           y = sorted(t)
           if x == y:
            return True
           else:
            return False 
        else:
            return False
        