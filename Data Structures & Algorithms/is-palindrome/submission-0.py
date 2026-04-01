class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for c in s:
            if c.isalnum():
                r += c.lower()
        for x in range(len(r)):
            if r[x] != r[len(r) - x - 1]:
                return False
        return True

        