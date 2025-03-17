# number of islands

# in this problem, we need to counte the number of islands

# these islands are represented by 1 in the grid and water by 0

# two ones can be connected if they are adjacent hoeizontally or vertically but not diagonally

# we should also count the lone ones as islands

# we use dfs

# we start from a cell with 1 and mark all the connected ones as visited

# we do this for all the cells in the grid

# the number of times we do this is the number of islands

# Time complexity: O(m*n) where m is the number of rows and n is the number of columns

# Space complexity: O(m*n) for the visited array

def numIslands(grid):
    if not grid:
        return 0  # Edge case - Empty grid

    rows, cols = len(grid), len(grid[0])
    visited = set()  # Tracks visited cells

    # DFS function to explore connected '1's
    def dfs(r, c):
        if (r < 0 or r >= rows or   # Out of bounds (top/bottom)
            c < 0 or c >= cols or   # Out of bounds (left/right)
            grid[r][c] == '0' or    # Water cell
            (r, c) in visited):     # Already visited
            return
        visited.add((r, c))         # Mark cell as visited
        
        # Explore all 4 directions
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)  # Explore the entire island
                count += 1  # Increment island count

    return count

