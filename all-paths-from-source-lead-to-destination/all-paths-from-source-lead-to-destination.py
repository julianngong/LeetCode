class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
        if destination in graph.keys():
            return False
        stack = [source]
        visited = [0 for _ in range(n)]
        while stack:
            current = stack[-1]
            visited[current] = 1
            if visited[current] ==2:
                stack.pop()
                continue
                
            for neighbours in graph[current]:
                if visited[neighbours] ==1:
                    return(False)
                elif visited[neighbours] == 0:
                    stack.append(neighbours)
            if current == stack[-1]:
                if (len(graph[current]) == 0) and (current != destination):
                    return(False)
                else:
                    visited[stack.pop()] =2
        return(True)