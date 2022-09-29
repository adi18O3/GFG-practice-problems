# Given an array of size N-1 such that it only contains distinct integers in the range 
# of 1 to N. Find the missing element.

def MissingNumber(self,array,n):

    sum_n = int((n*(n+1))/2)
        
    return sum_n - sum(array)