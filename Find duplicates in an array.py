def duplicates(self, arr, n): 
    # code here
    lst = [0 for i in range(n)]
    flst = []
    for i in arr:
        if(lst[i]==0):
            lst[i] += 1
        else:
            flst.append(i)
            
    if(len(flst)==0):
        return [-1]
        
    flst = list(set(flst))
    flst.sort()
    return flst