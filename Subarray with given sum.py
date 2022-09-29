# Given an unsorted array A of size N that contains only non-negative integers, 
# find a continuous sub-array which adds to a given number S.

# In case of multiple subarrays, return the subarray which comes first on moving from left to right.

def subArraySum(self,a, n, s): 
    sum = 0
    start = 0
    for i in range(n):
        sum += a[i]
            
        while(s<sum and start<i):
            sum -= a[start]
            start += 1

        if(sum==s):
            return [start+1 , i+1]
        
        
    return [-1]