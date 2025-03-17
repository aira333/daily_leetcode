# rotting oranges

from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()   # Queue for BFS
    fresh_count = 0   # Tracks number of fresh oranges

    # Add all rotten oranges to the queue and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, minute)
            elif grid[r][c] == 1:
                fresh_count += 1

    # Edge case: No fresh oranges from the start
    if fresh_count == 0:
        return 0

    # BFS Traversal
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
    minutes = 0

    while queue:
        r, c, minutes = queue.popleft()

        # Explore all 4 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # If within bounds and it's a fresh orange
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2  # Mark as rotten
                fresh_count -= 1  # Reduce fresh count
                queue.append((nr, nc, minutes + 1))

    #  Check for remaining fresh oranges
    return minutes if fresh_count == 0 else -1

