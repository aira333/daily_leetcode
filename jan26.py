class Solution:
    def maximumInvitations(self, A: List[int]) -> int:
        n, maxc = len(A), 0
        seen = [0] * n
        for idx in range(n):
            if seen[idx] == 0:
                start = idx
                cur_people = idx
                curset = set()

                while seen[cur_people] == 0:
                    seen[cur_people] = 1
                    curset.add(cur_people)
                    cur_people = A[cur_people]

                if cur_people in curset:
                    cursum = len(curset)
                    while start != cur_people:
                        cursum -= 1
                        start = A[start]
                    maxc = max(maxc, cursum)

        pair = []
        visited = [0] * n
        for i in range(n):
            if A[A[i]] == i and visited[i] == 0:
                pair.append([i, A[i]])
                visited[i] = 1
                visited[A[i]] = 1

        res = 0
        child = collections.defaultdict(list)
        for i in range(n):
            child[A[i]].append(i)

        for a, b in pair:
            maxa = 0
            dq = collections.deque()
            for cand in child[a]:
                if cand != b:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxa = max(maxa, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])

            maxb = 0
            dq = collections.deque()
            for cand in child[b]:
                if cand != a:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxb = max(maxb, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])

            res += 2 + maxa + maxb

        return max(maxc, res)
