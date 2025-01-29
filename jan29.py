class Solution(object):
    def findRedundantConnection(self, edges):
         
        n = len(edges)
        ds = [-1]*n
        def find(a):
            if ds[a]<0:
                return -ds[a], a
            else:
                t = find(ds[a])
                ds[a]=t[1]
                return t
        def union(a, b):
            rank1, root1 = find(a)
            rank2, root2 = find(b)
            if root1 != root2:
                if rank1>=rank2:
                  ds[root1]=-(rank1+rank2)
                  ds[root2]= root1
                else:
                  ds[root2]=-(rank1+rank2)
                  ds[root1]= root2
                return 0
            else:
                return 1

        for e in edges:
           if union(e[0]-1, e[1]-1):
             return e        