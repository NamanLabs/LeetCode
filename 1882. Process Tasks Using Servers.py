import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        
        busy_servers = []
        ans = []
        t = 0
        
        for j, time_needed in enumerate(tasks):
            t = max(t, j)
            
            if not free_servers:
                t = max(t, busy_servers[0][0])
                
            while busy_servers and busy_servers[0][0] <= t:
                free_time, w, i = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (w, i))
                
            w, i = heapq.heappop(free_servers)
            ans.append(i)
            heapq.heappush(busy_servers, (t + time_needed, w, i))
            
        return ans
