# critical connections in a network

# bridges in a graph problem

# Tarjan's algorithm

# Discovery time - disc[] - time when a node is first visited

# Lowest point of reachability - low[] - the earliest visited node that a node can reach using backtracking

# a connection is critical if low[neighbour] > disc[current_node]

# Approach - build an adjacency list to  represent the network

# start dfs from any node and track

# disc[] and low[]

# during dfs if low[neighbour] > disc[current_node] then the connection is critical

# collect all such connections in the result


from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        # Build the graph
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        #Initialize variables
        disc = [-1] * n         # Discovery time array
        low = [-1] * n          # Lowest reachable node array
        result = []             # Stores critical connections
        time = [0]              # Mutable time counter
        
        # DFS function
        def dfs(node, parent):
            disc[node] = low[node] = time[0]
            time[0] += 1
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Skip the parent node
                
                if disc[neighbor] == -1:  # If the neighbor is unvisited
                    dfs(neighbor, node)
                    # Update low-link value
                    low[node] = min(low[node], low[neighbor])
                    
                    # Check if it's a critical connection
                    if low[neighbor] > disc[node]:
                        result.append([node, neighbor])
                else:
                    # Backtracking step to update low value
                    low[node] = min(low[node], disc[neighbor])
        
        # Start DFS from node 0
        dfs(0, -1)
        
        return result
