import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        # Build Adjacency List
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Convert labels to numbers 0-25
        chars = [ord(c) - 97 for c in labels]
        
        # dist[u][char][count] stores the min weight to reach node u
        # with 'char' as the ending character and 'count' consecutive occurrences.
        # We can use a hash map for distance states to save memory.
        dist = {}
        
        start_char = chars[0]
        dist[(0, start_char, 1)] = 0
        
        # Priority Queue stores tuples: (current_weight, node, last_char, consecutive_count)
        pq = [(0, 0, start_char, 1)]
        
        while pq:
            w, u, last_char, count = heapq.heappop(pq)
            
            # Destination reached
            if u == n - 1:
                return w
                
            # If we've found a shorter path to this exact state already, skip
            if w > dist.get((u, last_char, count), float('inf')):
                continue
                
            for v, weight in adj[u]:
                v_char = chars[v]
                
                if v_char == last_char:
                    new_count = count + 1
                    if new_count > k:
                        continue  # Exceeds maximum allowed consecutive identical characters
                else:
                    new_count = 1
                    
                new_weight = w + weight
                
                if new_weight < dist.get((v, v_char, new_count), float('inf')):
                    dist[(v, v_char, new_count)] = new_weight
                    heapq.heappush(pq, (new_weight, v, v_char, new_count))
                    
        return -1
