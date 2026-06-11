class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(word1_index, word2_index):
            if word2_index >= len(word2):
                if word1_index < len(word1):
                    return len(word1) - word1_index
                else:
                    return 0
            if word1_index >= len(word1):
                return 1 + dfs(word1_index, word2_index + 1)
            
            if (word1_index, word2_index) in cache:
                return cache[(word1_index, word2_index)]
            
            res = 0

            if word1[word1_index] == word2[word2_index]:
                res += dfs(word1_index + 1, word2_index + 1)
            else:
                res += 1
                res += min(dfs(word1_index + 1, word2_index + 1), dfs(word1_index, word2_index + 1), 
                            dfs(word1_index + 1, word2_index))
            cache[(word1_index, word2_index)] = res
            return res

        return dfs(0, 0)