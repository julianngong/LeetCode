class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]: # if the top or bottom corners are 1 then return -1 automatically 
            return -1
        queue = deque([(0, 0, 1)]) # make a queue with co ords of first element being the starting node. the 3rd element of tuple represents steps gone
        seen = set([(0, 0)]) # make a seen list with element 0,0
        while queue:
            x, y, step = queue.popleft() #pop the queue setting the first two elements to the x y co ords in the queue and step being the current steps from top left
            if x == n - 1 and y == n - 1: # if we reach the bottom corner then return the number of steps it took to get there
                return step 
            for dx in (-1, 0, 1): # basically we can either step (+1,+1),(+1,0),(0,-1) etc so to get all these possibilities choose dx and dy to be any one of these 
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0: # but ignore the case when dx and dy both equal 0 as this means it doesnt move
                        continue 
                    nx, ny = x + dx, y + dy # make the new x and ney y co ord to be testing as followed
                    if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny] and (nx, ny) not in seen: # ensure that the new co ord is within the grid, that it is not 1 and that it has not been seen before
                        queue.append((nx, ny, step + 1)) # add it to the queue and move forward
                        seen.add((nx, ny)) # add it to the seen elements
        return -1 #else it has not been found so return -1
                
        