class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])
        # Create a new matrix to store the smoothed values
        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total_sum = 0
                count = 0
                
                # Traverse the 3x3 neighborhood around the current cell
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        # Boundary check: ensure the neighbor is inside the grid
                        if 0 <= r < m and 0 <= c < n:
                            total_sum += img[r][c]
                            count += 1
                            
                # Calculate the floor of the average
                res[i][j] = total_sum // count
                
        return res
