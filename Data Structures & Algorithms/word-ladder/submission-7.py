class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                key = w[0:i] + "*" + w[i + 1:]
                adjList[key].append(w)
        
        res = 0
        seen = set()
        queue = deque()
        queue.append(beginWord)
        seen.add(beginWord)
        while queue:
            res += 1
            for i in range(len(queue)):
                w = queue.popleft()
                if w == endWord:
                    return res
                for i in range(len(w)):
                    key = w[0:i] + "*" + w[i + 1:]
                    for nbr in adjList[key]:
                        if nbr not in seen:
                            queue.append(nbr)
                            seen.add(nbr)
                    adjList[key] = []
        return 0