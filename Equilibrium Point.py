def equilibriumPoint(self, a, n):
    # Your code here
    if(len(a)==1):
        return 1
        
    if(len(a)==2):
        return -1
    
    suml = a[0]
    mid = 1
    sumr = sum(a)-a[mid]-a[0]
    
    while(mid<n-1):
        if(suml == sumr):
            return mid+1
            
        suml += a[mid]
        mid += 1
        sumr -= a[mid]
     
    return -1