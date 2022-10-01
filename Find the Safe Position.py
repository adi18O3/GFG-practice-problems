
def safePos(self, n, k):
    if(n==1):
        return 1
    return (self.safePos(n-1,k)+k-1)%n + 1