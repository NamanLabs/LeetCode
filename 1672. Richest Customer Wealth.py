class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0 
        for i in accounts:
            current_wealth = sum(i)
            max_wealth = max (current_wealth, max_wealth)
        return max_wealth
