class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

  
        sus = set([k])
        stack = [k]

        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in sus:
                    sus.add(neighbor)
                    stack.append(neighbor)

        for u, v in invocations:
            if u not in sus and v in sus:
                return list(range(n))


        res = []
        for i in range(n):
            if i not in sus:
                res.append(i)

        return res