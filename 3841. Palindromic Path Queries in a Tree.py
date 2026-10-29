import sys

sys.setrecursionlimit(200000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 16
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        dist_mask = [0] * n
        s_chars = list(s)
        
        timer = 0
        
        # 1. Euler Tour and Binary Lifting via DFS
        def dfs(u, p, d, mask):
            nonlocal timer
            timer += 1
            in_time[u] = timer
            depth[u] = d
            up[u][0] = p
            
            for i in range(1, LOG):
                up[u][i] = up[up[u][i-1]][i-1]
                
            mask ^= (1 << (ord(s_chars[u]) - 97))
            dist_mask[u] = mask
            
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1, mask)
                    
            out_time[u] = timer

        dfs(0, 0, 0, 0)

        # 2. Fenwick Tree for Range Updates / Point Queries
        bit = [0] * (n + 2)
        
        def add(idx, val):
            while idx < len(bit):
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query_bit(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # 3. Lowest Common Ancestor (LCA)
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # 4. Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                old_c = s_chars[u]
                if old_c != c:
                    delta = (1 << (ord(old_c) - 97)) ^ (1 << (ord(c) - 97))
                    s_chars[u] = c
                    add(in_time[u], delta)
                    add(out_time[u] + 1, delta)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                m_u = dist_mask[u] ^ query_bit(in_time[u])
                m_v = dist_mask[v] ^ query_bit(in_time[v])
                m_lca_char = 1 << (ord(s_chars[lca]) - 97)
                
                path_mask = m_u ^ m_v ^ m_lca_char
                # Palindrome check: at most 1 bit set in path_mask
                ans.append(path_mask == 0 or (path_mask & (path_mask - 1)) == 0)
                
        return ans
