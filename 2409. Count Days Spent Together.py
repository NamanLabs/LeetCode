class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)
        
        if arrive > leave:
            return 0
            
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_days(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_per_month[:month - 1]) + day
            
        return date_to_days(leave) - date_to_days(arrive) + 1
