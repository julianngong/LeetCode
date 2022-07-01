class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        listzero = [0]
        queue = collections.deque()
        queue.append(listzero)
        seen = set(tuple([0]))
        paths = []
        while queue:
            currentpath = queue.popleft()
            currentnode = currentpath[-1]
            if currentnode == n-1:
                paths.append(currentpath)
            for neighbours in graph[currentnode]:
                if neighbours not in seen:
                    newpath = currentpath+[neighbours]
                    seen.add(tuple(newpath))
                    queue.append(newpath)
        return(paths)