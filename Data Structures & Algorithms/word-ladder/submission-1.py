class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        res = 0

        seen = set()
        adjList = defaultdict(list)

        for i in range(len(beginWord)):
                key = []
                for j in range(len(beginWord)):
                    if j == i:
                        key.append("*")
                    else:
                        key.append(beginWord[j])
                key = "".join(key)
                adjList[key].append(beginWord)

        for w in wordList:
            for i in range(len(w)):
                key = []
                for j in range(len(w)):
                    if j == i:
                        key.append("*")
                    else:
                        key.append(w[j])
                key = "".join(key)
                adjList[key].append(w)

        print(adjList)
        queue = deque()
        queue.append(beginWord)
        while queue:
            res += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return res
                seen.add(curr)
                for j in range(len(curr)):
                    key = []
                    for z in range(len(curr)):
                        if z == j:
                            key.append("*")
                        else:
                            key.append(curr[z])
                    key = "".join(key)
                    for z in adjList[key]:
                        if z not in seen:
                            queue.append(z)
                            seen.add(z)

        return 0


