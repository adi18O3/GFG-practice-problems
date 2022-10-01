class Solution:
    def leaders(self, a, n):
        #Code here
        m = 0
        lst = []
        for i in range(n,0,-1):
            if(a[i-1]>=m):
                lst.append(a[i-1])
                m = a[i-1]
        lst.sort(reverse=True)
        return lst