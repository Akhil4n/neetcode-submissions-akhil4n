class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = defaultdict(list)
        indegree = defaultdict(int)

        for w in words:
            for c in w:
                if c not in indegree:
                    indegree[c] = 0

        for i in range(0, len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            i = 0
            minLen = min(len(word1), len(word2))
            while i < minLen:
                if word1[i] != word2[i]:
                    break
                i += 1
            
            if i == minLen:
                if len(word1) > len(word2):
                    return ""
                continue

            adjList[word1[i]].append(word2[i])
            indegree[word2[i]] += 1

        res = []
        queue = deque()
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for nei in adjList[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        print(res)
        return "".join(res) if len(res) == len(indegree) else ""




