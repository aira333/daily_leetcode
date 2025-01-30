class Solution(object):
    def magnificentSets(self, n, edges):
        
        g = {}
        for i in range(n):
            g[i]=[]
        for e in edges:
            g[e[0]-1].append(e[1]-1)
            g[e[1]-1].append(e[0]-1)

        
        assigned = [-1]*n
        def bipartile(node): 
            stack = [(node, 0)]
            assigned[node]=0
            while stack:
                o, gr=stack.pop()
                for ad in g[o]:
                    if assigned[ad]!=-1:
                        if gr + assigned[ad]==1:
                            continue
                        else:
                            return -1
                    else:
                        if gr ==0:
                            assigned[ad]=1
                            stack.append((ad, 1))
                        else:
                            assigned[ad]=0
                            stack.append((ad, 0))
            return 1
        
        for i in range(n):
            if assigned[i]==-1:
                if bipartile(i)==-1:
                    return -1
        
        
        from collections import deque
        compo_with_max_lev = {}
        components = [-1]*n
        def max_level(node, com_id):
            
            visited = [False]*n
            q = deque()
            level = 1

            q.append((node, 1))
            visited[node]=True
            if com_id==-1:
                components[node] = node 
            while q:
                o, l = q.popleft()
                flag = False
                for ad in g[o]:
                    if not visited[ad]:
                        flag = True
                        visited[ad]=True
                        if com_id==-1:
                            components[ad] = node 
                        q.append((ad, l+1))
                if flag:
                    level = max(l+1, level)
            if com_id==-1:
                compo_with_max_lev[node]= level
            else:
                compo_with_max_lev[com_id]= max(level,compo_with_max_lev[com_id])

        for i in range(n):
           max_level(i, components[i])
        
        return sum(compo_with_max_lev.values())


                