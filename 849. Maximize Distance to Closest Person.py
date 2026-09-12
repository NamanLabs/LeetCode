class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        prev = -1
        max_dist = 0

        for i in range(n):
            if seats[i] == 1:
                if prev == -1:
                    # Edge case: Leading zeros
                    max_dist = i
                else:
                    # Middle segment between two occupied seats
                    max_dist = max(max_dist, (i - prev) // 2)
                prev = i

        # Edge case: Trailing zeros
        max_dist = max(max_dist, n - 1 - prev)

        return max_dist
