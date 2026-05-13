class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0

        adjList = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                key = w[0:i] + "*" + w[i + 1:]
                adjList[key].append(w)
        
        res = 0
        seen = set()
        queue = deque()
        queue.append(beginWord)

        while queue:
            res += 1
            for i in range(len(queue)):
                w = queue.popleft()
                if w == endWord:
                    return res
                if w in seen:
                    continue
                for i in range(len(w)):
                    key = w[0:i] + "*" + w[i + 1:]
                    for nbr in adjList[key]:
                        queue.append(nbr)
                seen.add(w)
        return 0