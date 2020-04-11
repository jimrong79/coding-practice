"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
"""

from heapq import heappush, heappop

def shortestPathBinaryMatrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    
    N = len(grid)
    
    if not grid or grid[0][0] == 1 or grid[N-1][N-1] == 1:
        return -1
    
    res = a_star_graph_search(
        start = (0,0),
        goal_function = get_goal_function(grid),
        successor_function = get_successor_function(grid),
        heuristic_function = get_heuristic_function(grid)
    )
    
    if res is None:
        return -1
    
    return len(res)
    
    

def a_star_graph_search( 
                         start,
                         goal_function,
                         successor_function,
                         heuristic_function                         
                        ):
    
    frontier = []
    heappush(frontier, (0, start))
    
    came_from = {}
    visited = set()
    steps = {start: 0}
    
    while frontier:
        priroty, node = heappop(frontier)
        
        if node in visited:
            continue
            
        if goal_function(node):
            return construct_path(came_from, start, node)
    
        visited.add(node)
    
        for successor in successor_function(node):
            priority = steps[node] + 1 + heuristic_function(successor)
            heappush(frontier, (priority, successor))
            
            if successor not in came_from or steps[successor] > steps[node] + 1:
                steps[successor] = steps[node] + 1
                came_from[successor] = node 
    
    return None
    

def get_goal_function( grid):
    M = len(grid)
    N = len(grid[0])

    def goal_function(cell):
        return cell == (M-1, N-1)
    
    return goal_function

def get_successor_function( grid):
    
    M = len(grid)
    N = len(grid[0])
    
    
    def successor_function(cell):
        i, j = cell
        return ((x + i, y + j) for x in (-1, 0, 1) for y in (-1, 0, 1)
                if x != 0 or y != 0
                if 0 <= x + i < M
                if 0 <= y + j < N
                if grid[x + i][y + j] == 0
               )
    return successor_function
    

def get_heuristic_function( grid):

    M = len(grid)
    N = len(grid[0])
    
    def heuristic_function(cell):
        return max(M - cell[0], N - cell[1])
    
    

    return heuristic_function
    
    

def construct_path( came_from, start, node):
    
    res = []
    
    while node != start:
        res.append(node)
        node = came_from[node]
    
    res.append(start)
    
    return list(reversed(res))


def main():
	grid = [[0,0,0,0,0,0,0,0,0],[0,1,1,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0],[0,1,0,0,1,1,0,0,1],\
	[0,0,1,0,0,1,0,0,1],[0,1,0,1,0,0,1,1,0],[0,0,0,0,0,1,0,0,0],[0,1,0,1,0,0,1,0,0],[0,1,1,0,0,0,0,1,0]]

	print (shortestPathBinaryMatrix(grid))


if __name__ == "__main__":
	main()
