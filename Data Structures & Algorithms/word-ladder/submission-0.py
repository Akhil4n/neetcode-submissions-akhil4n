class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        res = 0

        seen = set()
        adjList = defaultdict(list)

        for w in wordList:
            numDiff = 0
            for i in range(len(beginWord)):
                if beginWord[i] != w[i]:
                    numDiff += 1
                    if numDiff > 1:
                        break
            if numDiff > 1:
                continue
            adjList[beginWord].append(w)

        for i in range(len(wordList)):
            curr = wordList[i]
            for j in range(len(wordList)):
                if j == i:
                    continue
                numDiff = 0
                for z in range(len(curr)):
                    if curr[z] != wordList[j][z]:
                        numDiff += 1
                    if numDiff > 1:
                        break
                if numDiff > 1:
                        continue
                adjList[curr].append(wordList[j])
        queue = deque()
        queue.append(beginWord)
        while queue:
            res += 1
            print(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return res
                seen.add(curr)
                for j in adjList[curr]:
                    if j not in seen:
                        queue.append(j)
                        seen.add(j)

        return 0


