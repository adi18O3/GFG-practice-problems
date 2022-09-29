
def getMinDiff(self, arr, n, k):
    # code here
    arr.sort()
    maxo = arr[-1]
    mino = arr[0]
    dif = maxo-mino
    for i in range(1,n):
        maxo = max(arr[i-1]+k , arr[-1]-k)
        mino = min(arr[0]+k , arr[i]-k)
        if(mino>=0):
            dif = min(dif , maxo-mino)
    return dif