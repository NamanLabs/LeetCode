class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            needed_days = 1
            current_load = 0
            
            for w in weights:
                if current_load + w > capacity:
                    needed_days += 1
                    current_load = 0
                current_load += w
            
            return needed_days <= days

        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid  # Try finding a smaller valid capacity
            else:
                left = mid + 1  # Capacity too small, increase it
                
        return left
