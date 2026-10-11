class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current_altitude = 0
        max_altitude = 0
        
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)
            
        return max_altitude
