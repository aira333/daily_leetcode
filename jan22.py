class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(isWater)
        n = len(isWater[0])
        height = [[-1] * n for _ in range(m)] 
        queue = deque()  

       
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0  
                    queue.append((i, j))  

        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        
        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                newX, newY = x + dx, y + dy

               
                if 0 <= newX < m and 0 <= newY < n and height[newX][newY] == -1:
                    height[newX][newY] = height[x][y] + 1  
                    queue.append((newX, newY))  

        return height  