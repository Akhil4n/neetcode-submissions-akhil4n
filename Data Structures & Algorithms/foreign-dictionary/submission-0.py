class Solution:
    def foreignDictionary(self, words):
        res = []
        adj = {}
        ind = {}

        for w in words:
            for c in w:
                if c not in adj:
                    adj[c] = set()
                    ind[c] = 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        ind[w2[j]] += 1
                    break
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""

        q = deque()
        for c in ind:
            if ind[c] == 0:
                q.append(c)

        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in adj[curr]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)

        return "" if len(res) != len(ind) else "".join(res)

